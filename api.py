from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

app.config[‘UPLOAD_FOLDER‘]	= '/rules'
@app.route('/save', methods=["POST"])
def save():
    print("json", request.get_json())
    print("querystring", request.query_string.decode()) #parse
    return jsonify(success=True), 200
