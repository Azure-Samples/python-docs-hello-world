from flask import Flask,render_template,request,render_template_string
from elasticsearch import Elasticsearch
import requests
import json

app = Flask(__name__)

@app.route('/',methods=["get","post"])
def main():
    
    q1 = request.form.get("q")
    
    if q1 is not None:
        es = Elasticsearch(["https://elastic:EoDnxU5mTG90AT1tgO7uFUH4@e67c41f68a584eaead9f9108bc9e0800.us-east-1.aws.found.io:9243"])
        resp = es.search(index='kibana_sample_data_flights',doc_type='_doc',body={"query": {"match": {"Carrier": q1}}})
        for doc in resp['hits']['hits']:
            (doc['_id'],doc['_source']['FlightNum'])
        return render_template('index1.html',q=q1,response=(doc['_id'],doc['_source']['FlightNum']))
    
    return render_template('index1.html')

if __name__ == "__main__":
    app.run()

    