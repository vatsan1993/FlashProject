from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SECRET_KEY']='5a010e6170bd6627c422d94b9a2c1a46'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' # relative path

db= SQLAlchemy(app)


from Herezwhat import routes
