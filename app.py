from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect, session
from flask_security import Security, SQLAlchemyUserDatastore
from flask.ext.security.utils import encrypt_password
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
# from settings import *

app = Flask(__name__)

app.config.from_pyfile('config.py')

db=SQLAlchemy(app)

admin = Admin(app)

from models import *
from views import *

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Setup Admin panel
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Customer, db.session))
admin.add_view(ModelView(Child, db.session))


if __name__=="__main__":
    app.run()    