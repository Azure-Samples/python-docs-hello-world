from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World 1234!"

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')