from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/api/data', methods=['GET'])
def get_data():
    # Приклад даних для повернення
    data = {
        'message': 'Hello, this is your data!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    # Отримання даних з запиту
    content = request.json
    response_data = {
        'received': content,
        'status': 'success'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
