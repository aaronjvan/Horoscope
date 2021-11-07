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

@app.route('/horoscope', methods=['GET'])
def bday():
    birthMonth = request.args.get('m')
    birthDay = request.args.get('d')
    print(birthMonth, birthDay)
    return returnLink(birthMonth, birthDay)
    #return "https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask"