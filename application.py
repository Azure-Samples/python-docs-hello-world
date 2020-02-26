from flask import Flask
import azure-ai-textanalytics
app = Flask(__name__)

@app.route("/")
def hello():
    return "running 1"


#from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
#from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
#print(dir())
#print("Hola")
