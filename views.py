from app import app, db
from flask_security import login_required
from flask import render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from forms import *
from models import *

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

@app.route('/add_customer', methods=['GET','POST'])
@login_required
def add_customer():
    form = CustomerEntryForm()

    if request.method == 'POST':
        if form.validate():
            customer = Customer(first_name=request.form['first_name'],last_name=request.form['last_name'],email=request.form['email'],street_address=request.form['street_address']
                       ,suburb=request.form['suburb'],state=request.form['state'],postcode=request.form['postcode'],phone=request.form['phone']
                       ,alternative_contact=request.form['alternative_contact'],alternative_contact_phone=request.form['alternative_contact_phone'],notes=request.form['notes'])
            form.populate_obj(customer)
            # entry.id=1
            db.session.add(customer)
            db.session.commit()
            # flash('New entry was successfully posted')
            return render_template('success.html')
        else:
            # flash("Your form contained errors")
            return render_template('/add_customer.html', form=form)
    elif request.method == 'GET': 
        return render_template('/add_customer.html', form=form)    

    

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

@app.route('/customer_admin/')
@login_required
def customer_admin():
    return render_template('/customer_admin.html')     