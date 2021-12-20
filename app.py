# from requests import request
import json
from flask import Flask, request,  jsonify
from datetime import datetime
import pyodbc
import random


app = Flask(__name__)

server = 'dblocator.database.windows.net'
database = 'locatorserver'
username = 'AdminLocator'
password = 'LovelyLocator1!'
driver = '{ODBC Driver 17 for SQL Server}'

sCon = 'DRIVER='+driver+';SERVER=tcp:'+server + \
    ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password


def InsertWifi(ssid, mac, level, phoneid, dt):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.Wifi(ssid, mac, level, phoneid,dt) VALUES (?,?,?,?,?) "

        mycursor.execute(sql, (ssid, mac, level, phoneid, dt))
        con.commit()
        con.close()
        return "Succeded"
    except Exception as ex:
        return str(ex)


def GetDefaultConfigLine(phoneid):
    dic = {}
    dic['phoneid'] = phoneid
    dic['wifiInterval'] = 2
    dic['BluetoothInterval'] = 2
    dic['locationInterval'] = 1
    dic['checkConfigInterval'] = 3
    dic['StartTimeActivation'] = 1
    dic['StopTimeActivation'] = 3
    dic['AllTime'] = "True"
    dic['ActivateWifi'] = 0
    dic['ActivateBlueTooth'] = 0
    dic['ActivateWifiDateTime'] = "01-01-99 16:40:19"
    dic['ActivateBlueToothDateTime'] = "01-01-99 16:40:19"
    dic['ActivateWifiDuration'] = 0
    dic['ActivateBlueToothDuration'] = 0
    s = json.dumps(dic)
    # xx
    return s


def GetlastConfigLine(phoneid):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "SELECT top 1 * FROM config where phoneid='"+phoneid+"' order by id desc"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        dic = {}
        for row in myresult:
            dic['phoneid'] = row[1]
            dic['wifiInterval'] = row[2]
            dic['BluetoothInterval'] = row[3]
            dic['locationInterval'] = row[4]
            dic['checkConfigInterval'] = row[5]
            dic['StartTimeActivation'] = row[6]
            dic['StopTimeActivation'] = row[7]
            dic['AllTime'] = row[8]
            dic['ActivateWifi'] = row[9]
            dic['ActivateBlueTooth'] = row[10]
            try:

                ActivateWifiDateTime = row[11].strftime('%d-%m-%y %H:%M:%S')
                ActivateBlueToothDateTime = row[12].strftime(
                    '%d-%m-%y %H:%M:%S')
                dic['ActivateWifiDateTime'] = ActivateWifiDateTime
                dic['ActivateBlueToothDateTime'] = ActivateBlueToothDateTime

            except Exception as ex:
                return str(ex)
            dic['ActivateWifiDuration'] = row[13]
            dic['ActivateBlueToothDuration'] = row[14]

        con.close()
        s = json.dumps(dic)
        return s
    except Exception as ex:
        return str(ex)


def InsertConfig(phoneid, wifiInterval,
                 BluetoothInterval, locationInterval, checkConfigInterval, StartTimeActivation,
                 StopTimeActivation, AllTime, ActivateWifi, ActivateBlueTooth, ActivateWifiDateTime, ActivateBlueToothDateTime, ActivateWifiDuration, ActivateBlueToothDuration):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.config(phoneid, wifiInterval," + \
            "BluetoothInterval, locationInterval,checkConfigInterval,StartTimeActivation," +\
            "StopTimeActivation,AllTime,ActivateWifi,ActivateBlueTooth,ActivateWifiDateTime,ActivateBlueToothDateTime,ActivateWifiDuration,ActivateBlueToothDuration)" +\
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) "

        mycursor.execute(sql, (phoneid, wifiInterval,
                               BluetoothInterval, locationInterval, checkConfigInterval, StartTimeActivation,
                               StopTimeActivation, AllTime, ActivateWifi, ActivateBlueTooth, ActivateWifiDateTime, ActivateBlueToothDateTime, ActivateWifiDuration, ActivateBlueToothDuration))
        con.commit()
        con.close()
        return "Succeded"
    except Exception as ex:
        return str(ex)


def InsertPhoneInfo(phoneid, phonenumber, imei, serialNumber, simOperator, dt, manufacturer, model, version, versionRelease):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.phone(phoneid, phonenumber, imei, serialNumber, simOperator,dt, manufacturer, model, version, versionRelease) VALUES (?,?,?,?,?,?,?,?,?,?) "

        mycursor.execute(sql, (phoneid, phonenumber, imei,
                         serialNumber, simOperator, dt, manufacturer, model, version, versionRelease))
        con.commit()
        con.close()
        return "Succeded"
    except Exception as ex:
        return str(ex)


def InsertBluetooth(name, code, address, rssi, phoneid, dt):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.Bluetooth(namex, codex,addressx,rssi,phoneid,dt) VALUES (?,?,?,?,?,?) "

        mycursor.execute(sql, (name, code, address, rssi, phoneid, dt))
        con.commit()
        con.close()
        return "Succeded"
    except Exception as ex:
        return str(ex)


def InsertLocation(lot, lat, dt, phoneid, accuracy, speed, sendTime):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.Location(Longitute, Latitude,dt,phoneid,accuracy,speed,SendTime) VALUES (?,?,?,?,?,?,?) "

        mycursor.execute(sql, (lot, lat, dt, phoneid,
                         accuracy, speed, sendTime))
        con.commit()
        con.close()
        return "Succeded2"
    except Exception as ex:
        return str(ex)


@app.route("/testconnection")
def TestConnectio():
    return "Works"


@app.route("/bluetooth", methods=['POST'])
def bluetooth():
    data = request.get_data()
    sData = data.decode('utf-8')
    d = json.loads(sData)
    name = d['name']
    code = d['code']
    address = d['address']
    rssi = d['rssi']
    phoneid = d['phoneid']
    dt = d['dt']

    try:
        date_time_obj = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)
    return InsertBluetooth(name, code, address, rssi, phoneid, date_time_obj)

# Post
# http://127.0.0.1:5000/config
# payload
# {"phoneid":"7406b194-a792-4bb2-9bfb-3a6d0ff74957","wifiInterval":1,"BluetoothInterval":2,"locationInterval":3,"checkConfigInterval":4,"StartTimeActivation":"16:31:19",
# "StopTimeActivation":"16:41:19","StartTimeActivation":13,"StopTimeActivation":14,"AllTime":1,"ActivateWifi":0,"ActivateBlueTooth":1,
#   "ActivateWifiDateTime":"11/11/21 16:31:19","ActivateBlueToothDateTime":"11/11/21 17:31:19","ActivateWifiDuration":5,"ActivateBlueToothDuration":6}
#
# get
# https://locatorwb.azurewebsites.net/config?phoneid=7406b194-a792-4bb2-9bfb-3a6d0ff74957
# in get version the function will get the last line of config that relates to the phoneid


@app.route("/config", methods=['GET', 'POST'])
def config():
    if (request.method == 'POST'):
        data = request.get_data()
        sData = data.decode('utf-8')
        d = json.loads(sData)
        phoneid = d['phoneid']  # guid identifying the phone
        wifiInterval = d['wifiInterval']  # interval in minutes
        BluetoothInterval = d['BluetoothInterval']  # interval in minutes
        locationInterval = d['locationInterval']  # interval in minutes
        checkConfigInterval = d['checkConfigInterval']  # interval in minutes
        # number: hour from 1-24
        StartTimeActivation = d['StartTimeActivation']
        StopTimeActivation = d['StopTimeActivation']  # number: hour from 1-24
        # boolean if true will activate all time no matter what StartTimeActivation and StopTimeActivation are.
        AllTime = d['AllTime']
        # boolean if true will activate wifi from ActivateWifiDateTime (dateTime) for  ActivateWifiDuration minutes
        ActivateWifi = d['ActivateWifi']
        # boolean if true will activate wifi from ActivateBlueToothDateTime (dateTime) for  ActivateBlueToothDuration minutes
        ActivateBlueTooth = d['ActivateBlueTooth']
        # the datetime to start activate wifi if ActivateWifi is true
        ActivateWifiDateTime = d['ActivateWifiDateTime']
        # the datetime to start activate blueTooth if ActivateWifi is true
        ActivateBlueToothDateTime = d['ActivateBlueToothDateTime']
        # the duration of wifi activation
        ActivateWifiDuration = d["ActivateWifiDuration"]
        # the duration of bluetooth activation
        ActivateBlueToothDuration = d["ActivateBlueToothDuration"]

        try:
            wifiDate = datetime. strptime(
                ActivateWifiDateTime, '%d/%m/%y %H:%M:%S')
            blueToothDate = datetime. strptime(
                ActivateBlueToothDateTime, '%d/%m/%y %H:%M:%S')
        except Exception as ex:
            print(ex)

        try:
            ret = InsertConfig(phoneid, wifiInterval,
                               BluetoothInterval, locationInterval, checkConfigInterval, StartTimeActivation,
                               StopTimeActivation, AllTime, ActivateWifi, ActivateBlueTooth, wifiDate, blueToothDate, ActivateWifiDuration, ActivateBlueToothDuration)
            return ret
        except Exception as ex:
            return str(ex)
    else:
        try:
            phoneid = request.args["phoneid"]
            ret = GetlastConfigLine(phoneid)
            if (ret == '{}'):
                return GetDefaultConfigLine(phoneid)

            return ret
        except Exception as ex:
            return GetDefaultConfigLine(phoneid)
            # return str(ex)


@app.route("/wifi", methods=['POST'])
def wifi():
    data = request.get_data()
    sData = data.decode('utf-8')
    d = json.loads(sData)
    ssid = d['ssid']
    mac = d['mac']
    level = d['level']
    phoneid = d['phoneid']
    dt = d['dt']
    try:
        date_time_obj = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)
    return InsertWifi(ssid, mac, level, phoneid, date_time_obj)


@app.route("/setup", methods=['POST'])
def setup():
    data = request.get_data()
    sData = data.decode('utf-8')
    d = json.loads(sData)
    serialNmber = d['serialNumber']
    imei = d['imei']
    phonenumber = d['phonenumber']
    simOperator = d['simOperator']
    phoneid = d['phoneid']
    dt = d['dt']
    manufacturer = d["manufacturer"]
    model = d["model"]
    version = d["version"]
    versionRelease = d["versionRelease"]
    try:
        date_time_obj = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)

    return InsertPhoneInfo(phoneid, phonenumber, imei,
                           serialNmber, simOperator, date_time_obj, manufacturer, model, version, versionRelease)


@ app.route("/location", methods=['POST'])
def location():

    data = request.get_data()
    sData = data.decode('utf-8')
    d = json.loads(sData)
    x = 1
    Longitute = d['longitude']
    Latitude = d['latitude']
    dt = d['datetime']
    phoneid = d['phoneid']
    accuracy = d['accuracy']
    speed = d['speed']
    sendTime = d['sendTime']

    try:
        date_time_obj = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)

    try:
        sendTimeStr = datetime. strptime(sendTime, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)

    return InsertLocation(Longitute, Latitude, date_time_obj, phoneid, accuracy, speed, sendTimeStr)


@ app.route("/getName")
def getName():
    dic = {}
    dic["name"] = "xxxx"
    dic["age"] = 23
    dic["num"] = 17
    data = json.dumps(dic)

    return data


def InsertLoLog(phoneid, dt, msg):
    try:
        con = pyodbc.connect(sCon)
        mycursor = con.cursor()
        sql = "INSERT INTO dbo.Logs(phoneid, dt, msg) VALUES (?,?,?) "

        mycursor.execute(sql, (phoneid, dt, msg))
        con.commit()
        con.close()
        return "Succeded"
    except Exception as ex:
        return str(ex)


@app.route("/log",  methods=['POST'])
def Log():
    data = request.get_data()
    sData = data.decode('utf-8')
    d = json.loads(sData)
    dt = d['dt']
    phoneid = d['phoneid']
    msg = d["msg"]
    try:
        date_time_obj = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')
    except Exception as ex:
        print(ex)
    return InsertLoLog(phoneid, date_time_obj, msg)


@ app.route("/")
def hello():
    try:
        con = pyodbc.connect(sCon)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        s = ""
        for row in rows:
            for field in row:
                s += str(field)+" "

        print("Handling request to home page.")
        con.close()
        return "Hello, Azure2!"+s
    except Exception as ex:
        return (str(ex))


# app.run()
