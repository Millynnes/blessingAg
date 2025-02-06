import logging
from flask import Flask, render_template, request, jsonify
from fortune_calculator import calculate_fortune

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'fortune2025secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_fortune', methods=['POST'])
def get_fortune():
    try:
        birthday = request.form.get('birthday')
        if not birthday:
            return jsonify({'error': '请输入生日'}), 400
        
        fortune = calculate_fortune(birthday)
        return jsonify(fortune)
    except Exception as e:
        logging.error(f"Error calculating fortune: {str(e)}")
        return jsonify({'error': '计算运势时出错'}), 500
