from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Health Monitoring System will be deployed soon"
