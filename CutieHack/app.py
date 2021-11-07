from flask import Flask, request
from flask_cors import CORS
from main import *

app = Flask(__name__)

CORS(app)
@app.route('/')
def index():
	return "Hello World!"

@app.route('/test')
def test():
	return "Hello test!"

#@app.route('getHoroscope', methods=['GET'])
#def horoscope('/horoscope')

@app.route('/horoscope', methods=['GET'])
def horoscope():
    birthMonth = request.args.get('m')
    birthDay = request.args.get('d')
    return returnHoroscope(birthMonth, birthDay)
    #return "https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask"

@app.route('/playlist', methods=['GET'])
def songLink():
    birthMonth = request.args.get('m')
    birthDay = request.args.get('d')
    return returnLink(birthMonth, birthDay)