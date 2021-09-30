from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/index")
def index():
    return render_template('index.html')



