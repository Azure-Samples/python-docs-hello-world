from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



@app.route("/")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')





class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key = True)
	user = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(64))
	azure_item_id = db.Column(db.String(64))

	def __repr__(self):
		return '<User %r>' % self.username


