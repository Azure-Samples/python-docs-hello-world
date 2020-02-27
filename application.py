from flask import Flask
from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
app = Flask(__name__)

@app.route("/")
def hello():
    return "running 4"
