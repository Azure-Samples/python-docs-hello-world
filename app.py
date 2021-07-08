from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello, World 12345!"

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')





class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(64))
	azure_item_id = db.Column(db.String(64))

	def __repr__(self):
		return '<User %r>' % self.username


itorres = User(email='itorres@deepdatas.com', password='1234', azure_item_id='test_id')
fbloise = User(email='fbloise@deepdatas.com', password='2345', azure_item_id='test_id')
mgarcia = User(email='mgarcia@deepdatas.com', password='3456', azure_item_id='test_id')

db.session.add_all([itorres, fbloise, mgarcia])

db.session.commit()

db.drop_all()

db.create_all()

print(itorres.email)