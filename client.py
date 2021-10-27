from datetime import datetime
import mysql.connector

mydb = None
try:
    x = 0
    mydb = mysql.connector.connect(user="locationadmin@locatormysqlserver1", password="LovelyLocation1",
                                   host="locatormysqlserver1.mysql.database.azure.com", database="sys")
    print(mydb)
    x = 1
except Exception as ex:
    print(ex)
