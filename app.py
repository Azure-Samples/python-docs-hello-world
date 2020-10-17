from flask import Flask
import mysql.connector
app = Flask(__name__)

server = "dripper.mysql.database.azure.com"
database = "greenhouse"
username = "points"
password = "Dripper#1"
# MySQL configurations
cnxn = mysql.connector.connect(host=server,database=database,username=username, password=password, autocommit=True)
cursor = cnxn.cursor()

@app.route("/")
def hello():
    cursor.execute("SELECT * FROM stats")
    myresult = cursor.fetchall()
    result = ""
    for row in myresult:
        print(row)
        result = result + str(row)

    return result
