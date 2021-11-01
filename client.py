from datetime import datetime
import mysql.connector
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)


mydb = None
try:
    x = 0
    #hostx = "52.128.23.153"
    hostx = "locatormysqlserver.mysql.database.azure.com"
    userx = "LocationAdmin1@locatormysqlserver"

    mydb = mysql.connector.connect(user=userx, password="LovelyLocation1!",
                                   host=hostx, port=3306)
    print(mydb)
    x = 1
except Exception as ex:
    print(ex)
