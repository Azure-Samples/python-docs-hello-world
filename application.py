from flask import Flask
from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
app = Flask(__name__)

@app.route("/")
def hello():
    return "running 3"
