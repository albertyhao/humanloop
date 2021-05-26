from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/save', methods=["POST"])
def save():
    print(request.get_json())
    print(request.query_string.decode()) #parse
    return jsonify(success=True), 200
