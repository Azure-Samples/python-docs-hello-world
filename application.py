from flask import Flask
import pandas
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola World!"

#from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
#from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
#print(dir())
#print("Hola")
