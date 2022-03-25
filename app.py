import os
import logging

from flask import Flask

app = Flask(__name__)

@app.route('/status')
def health_check():
    app.logger.info('Status request successfull')
    app.logger.debug('DEBUG message')

    return 'OK - healthy'

@app.route('/metrics')
def metrics():
    app.logger.info('Metrics request successfull')
    app.logger.debug('DEBUG message')

    return 'OK - metrics'

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    app.logger.info('Main request successfull')
    app.logger.debug('DEBUG message')

    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
