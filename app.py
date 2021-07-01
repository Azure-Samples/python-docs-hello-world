from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World 1234!"


@app.route("/hola")
def hola():
    return "<h1 style="color:orange;">Hello, Deepdatas 1234!</h1>"
