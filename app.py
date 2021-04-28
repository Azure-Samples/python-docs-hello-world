import os

import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions

from flask import Flask
app = Flask(__name__)

HOST = os.environ.get('COSMOSDB_URI', 'localhost')
MASTER_KEY = os.environ.get('SQLCONNSTR_RO_PRIMARY', 'XXX')

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )

def list_databases(client):
    print("\n4. List all Databases on an account")
    print('Databases:')

    databases = list(client.list_databases())

    if not databases:
        return

    for database in databases:
        return database['id']


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/list")
def get_list():
    try:
        return list_databases(client)
    except Exception as e:
        return "error"