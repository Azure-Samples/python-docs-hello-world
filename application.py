from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Swati, Trying to deploy Python flask application!"
