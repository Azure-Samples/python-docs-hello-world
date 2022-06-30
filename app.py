from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hiii, Meri Khoobsurat Larki :))!"


