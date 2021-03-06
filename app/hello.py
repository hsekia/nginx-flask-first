import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    app.logger.info("called hello_world")
    return "Hello World!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
