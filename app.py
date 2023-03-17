from flask import Flask
from time1 import get_time
from date import get_date

app = Flask(__name__)

@app.route('/time')
def time():
    return get_time()

@app.route('/date')
def date():
    return get_date()

@app.route('/hello')
def hello():
    return 'Hello Omar'

if __name__ == '__main__':
    app.run()
