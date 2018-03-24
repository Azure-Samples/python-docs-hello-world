from flask import flash, Flask, jsonify, render_template,request, make_response, url_for, redirect, session
from flask_cors import CORS, cross_origin
from passlib.hash import sha256_crypt
from functools import wraps, update_wrapper
from random import *
import time
import datetime


app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
