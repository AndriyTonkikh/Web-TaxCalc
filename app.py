from flask import Flask, request, jsonify, render_template
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer
from opencensus.ext.flask.flask_middleware import FlaskMiddleware

app = Flask(__name__)


exporter = AzureExporter(connection_string="InstrumentationKey=09269765-812a-4bed-a6dc-5b273e607a6d")
tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(1.0))

# Додаємо Application Insights до Flask Middleware для автоматичного відстеження запитів
middleware = FlaskMiddleware(app, exporter=exporter, sampler=ProbabilitySampler(1.0))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    with tracer.span(name="get_data_span"):
        data = {
            'message': 'Hello, this is your data!',
            'status': 'success'
        }
    return jsonify(data)

@app.route('/api/greet/<name>', methods=['GET'])
def greet_user(name):
    with tracer.span(name="greet_user_span"):
        greeting = f"Hello, {name}! Welcome to the Flask Application!"
    return jsonify({'greeting': greeting, 'status': 'success'})

@app.route('/api/data', methods=['POST'])
def post_data():
    with tracer.span(name="post_data_span"):
        content = request.json
        response_data = {
            'received': content,
            'status': 'success'
        }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
