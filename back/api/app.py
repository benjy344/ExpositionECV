#! /usr/bin/env python3
from flask import Flask
from flask.ext.bootstrap import Bootstrap
import os.path
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
Bootstrap(app)


def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__),p))


app.config['SQLALCHEMY_DATABASE_URI']=('sqlite:///'+mkpath('../api.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']="1efbd05d-e70c-454c-9200-50ab6d982eba"
db=SQLAlchemy(app)
from flask.ext.login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login"


from flask_cors import CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})