import subprocess
import sys
from subprocess import Popen, PIPE
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

print(subprocess.run(['pylint', 'api.py'], text=True).stdout)

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

@app.route('/test', methods=["POST"])
def test():
    try:
        userCode = request.get_json()['code']
        print(userCode)
        file = open('tmp.py', 'w')
        print("1")
        file.write(userCode)

        output = subprocess.run(['cat', '/Users/alberthao/desktop/github/humanloop/tmp.py'], check=True, text=True, capture_output=True)
        print(output)
        file.close()
        return "OK"
    except Exception as ex:
        print(2)
        print(ex)
        return ex

    # with Popen(['pylint', ' api.py'], stdout=PIPE, universal_newlines=True, shell=True) as output:
    #     print("inside")
    #     print(output.stdout.read())
