from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect, session
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
import os
# from settings import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL') + "?sslmode=require"
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY') 
app.config['SECURITY_REGISTERABLE']= os.environ.get('SECURITY_REGISTERABLE') 
app.config['SECURITY_PASSWORD_HASH'] = os.environ.get('SECURITY_PASSWORD_HASH')  
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT') 
db=SQLAlchemy(app)

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(255), unique=True)
    street_address = db.Column(db.String(150))
    suburb = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postcode = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    alternative_contact = db.Column(db.String(100))
    alternative_contact_phone = db.Column(db.String(50))
    notes = db.Column(db.String(255))                            

class Child(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer(), db.ForeignKey('customer.id'))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    notes= db.Column(db.String(255)) 

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html', user=user)

@app.route('/post_user', methods=['POST'])
def post_user():
   user = User(request.form['username'],request.form['email'])
   db.session.add(user)
   db.session.commit() 
   return redirect(url_for('index'))

# Navigation 
@app.route('/')
@login_required
def index():
    return render_template('/index.html')

@app.route('/add_customer/')
@login_required
def add_customer():
    return render_template('/add_customer.html')

@app.route('/add_class_member/')
@login_required
def add_class_member():
    return render_template('/add_class_member.html')

@app.route('/add_class/')
@login_required
def add_class():
    return render_template('/add_class.html') 

@app.route('/add_expense/')
@login_required
def add_expense():
    return render_template('/add_expense.html') 

@app.route('/add_payment/')
@login_required
def add_payment():
    return render_template('/add_payment.html')    

   
if __name__=="__main__":
    app.debug=True  
    app.run()    