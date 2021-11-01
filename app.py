#from requests import request
import json
from flask import Flask, request,  jsonify
from datetime import datetime


app = Flask(__name__)


# def InsertLocation(lot, lat, phoneid, dt):
#     mycursor = mydb.cursor()
#     sql = "INSERT INTO location (lot, lat,phoneid,dt) VALUES (%s, %s,%d,%d)"
#     val = (lot, lat, phoneid, dt)
#     mycursor.execute(sql, val)
#     mydb.commit()


@app.route("/testconnection")
def TestConnectio():
    return "Works"


@app.route("/")
def hello():
    print("Handling request to home page.")
    return "Hello, Azure1!"


# @app.route("/location", methods=['POST'])
# def Location():
#     try:
#         content = request.get_json()
#         lot = content["longitude"]
#         lat = content["latitude"]
#         sdt = content["datetime"]
#         phoneid = content["phoneid"]
#         dt = datetime.strptime(sdt, '%d/%m/%y %H:%M:%S')
#         InsertLocation(lot, lat, phoneid, dt)

#         data = json.dumps(content)
#         print(data)
#         # datetime = request.form.get('datetime')
#         # longitude = request.form.get('longitude')
#         # Latitude = request.form.get('latitude')
#         # phoneid = request.form.get('phoneid')
#     except Exception as ex:
#         print(ex)


# app.run()
