from flask import Flask
import azure-ai-textanalytics
app = Flask(__name__)

@app.route("/")
def hello():
    return "running 3"
