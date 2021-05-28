import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

app.config['UPLOAD_FOLDER']	= '/rules'
@app.route('/save', methods=["POST"])
def save():
    userCode = request.get_json()['text'] #take text from request for code

    filename = request.query_string.decode().split('=')[1] #parse
    #create new file
    file = open(filename, "w")
    file.write(userCode)
    file.close()
    return jsonify(success=True), 200

@app.route('/python', methods=["POST"])
def python():
