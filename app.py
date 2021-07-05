from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World 1234!"


@app.route("/login")
def hello():
    render_template('login.html')