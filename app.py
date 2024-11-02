from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, this is your data!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/greet/<name>', methods=['GET'])
def greet_user(name):
    greeting = f"Hello, {name}! Welcome to the Flask Application!"
    return jsonify({'greeting': greeting, 'status': 'success'})

@app.route('/api/data', methods=['POST'])
def post_data():
    content = request.json
    response_data = {
        'received': content,
        'status': 'success'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
