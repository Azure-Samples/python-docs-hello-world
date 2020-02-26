from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return print(dir())


#from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
#from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
#print(dir())
#print("Hola")
