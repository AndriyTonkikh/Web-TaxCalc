from flask import Flask, request, jsonify, render_template
from applicationinsights import TelemetryClient

app = Flask(__name__)


instrumentation_key = ''
telemetry_client = TelemetryClient(instrumentation_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, this is your data!',
        'status': 'success'
    }
    telemetry_client.track_event('Get Data Endpoint Accessed')
    return jsonify(data)

@app.route('/api/greet/<name>', methods=['GET'])
def greet_user(name):
    greeting = f"Hello, {name}! Welcome to the Flask Application!"
    telemetry_client.track_event('Greet User Endpoint Accessed', {'name': name})
    return jsonify({'greeting': greeting, 'status': 'success'})

@app.route('/api/data', methods=['POST'])
def post_data():
    content = request.json
    response_data = {
        'received': content,
        'status': 'success'
    }
    telemetry_client.track_event('Post Data Endpoint Accessed', {'data': content})
    return jsonify(response_data)

@app.before_first_request
def before_first_request():
    telemetry_client.track_event('Application Started')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    telemetry_client.flush()
    return jsonify({'status': 'shutdown initiated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
