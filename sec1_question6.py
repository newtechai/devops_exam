from flask import Flask, request
from logzero import logger
from statsd import StatsClient

app = Flask(__name__)
statsd_client = StatsClient(host='localhost', port=8125)

@app.route('/')
def hello():
    logger.info('Hello route is called')
    return 'Hello, sir'

@app.route('/error')
def error():
    try:
        raise Exception('An exception occurred')
    except Exception as e:
        logger.error('Exception occurred', exc_info=True)
        statsd_client.incr('exceptions')
        return 'Error occurred'

if __name__ == '__main__':
    logger.info('Starting Flask application')
    app.run()
# to run the app use python sec1_question6.py