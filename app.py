from flask import Flask, request
from time1 import get_time1
from date import get_date

app = Flask(__name__)

@app.route('/api/time', methods=['GET']) 

def get_time(): 

    api_type = request.args.get('tipo_api', 'hour') # Get the requested API type, default to 'hour' 

    if api_type == 'hour': 

        return get_time1() # Respond with the current hour in 24-hour format 

    elif api_type == 'date': 

        return get_date() # Respond with the current datetime in YYYY-MM-DD HH:MM:SS format 
    
    elif api_type == "mensaje":

        return "Hello Omar!"

    else: 

        return 'Invalid API type requested. Valid types are "hour" and "datetime"'

@app.route('/date')
def date():
    return get_date()

@app.route('/hello')
def hello():
    return 'Hello Omar'

if __name__ == '__main__':
    app.run()
