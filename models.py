from flask_security import  UserMixin, RoleMixin
from app import db

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
    postcode = db.Column(db.Integer())
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

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Customer, db.session))