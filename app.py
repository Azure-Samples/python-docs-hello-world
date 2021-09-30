from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    return render_template('index.html')



