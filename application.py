from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    a = print(dir())
    return a


#from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
#from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
#print(dir())
#print("Hola")
