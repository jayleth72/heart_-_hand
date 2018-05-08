from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect, session
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
import os
# from settings import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL') + "?sslmode=require"
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY') 
app.config['SECURITY_REGISTERABLE']= os.environ.get('SECURITY_REGISTERABLE') 
app.config['SECURITY_PASSWORD_HASH'] = os.environ.get('SECURITY_PASSWORD_HASH')  
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT') 
db=SQLAlchemy(app)

admin = Admin(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from views import *

if __name__=="__main__":
    app.debug=True  
    app.run()    