from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect, session
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
from settings import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= DATABASE_PASSWORD
app.config['SECRET_KEY']= SECRET_KEY 
app.config['SECURITY_REGISTERABLE']= SECURITY_REGISTERABLE
app.config['SECURITY_PASSWORD_HASH'] = SECURITY_PASSWORD_HASH 
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT 
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

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
@login_required
def index():
    return render_template('/index.html')


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
   
if __name__=="__main__":
    app.debug=True  
    app.run()    