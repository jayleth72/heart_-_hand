from app import app, db
from flask_security import login_required
from flask import render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from forms import *
from models import *
from flask_table import Table, Col
import sys

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
            
            db.session.add(customer)
            db.session.commit()
            flash('New customer was successfully added')
            return redirect(url_for('add_child', arg1=request.form['first_name'],arg2=request.form['last_name'], arg3=request.form['email']))
        else:
            flash("Your form contained errors")
            return redirect(url_for('add_customer'))
     
    return render_template('add_customer.html', form=form)    


@app.route('/add_child', methods=['GET','POST'])
@login_required
def add_child():

    form = ChildEntryForm()
    if 'arg1' in request.args:
        first_name = request.args['arg1']
    if 'arg2' in request.args:    
        last_name = request.args['arg2']
    if 'arg3' in request.args:    
        email = request.args['arg3']
        # get customer id for insertion as foreign key in child table
        customer = Customer.query.filter_by(email=email).first()
   
    if request.method == 'POST':
         if form.validate():
             child = Child(parent_id=customer.id,first_name=request.form['first_name'],last_name=request.form['last_name'],date_of_birth=request.form['date_of_birth'],notes=request.form['notes'])
             form.populate_obj(child)
             db.session.add(child)
             db.session.commit()
             flash('New child was successfully added')
             return redirect(url_for('success')) 
         else:
             flash("Your form contained errors")
             return redirect(url_for('add_child', arg1=first_name, arg2=last_name, arg3=email))
    
    return render_template('/add_child.html', first_name=first_name, last_name=last_name, email=email, form=form)  


@app.route('/search_customers', methods=['GET','POST'])
@login_required
def search_customers():
    search = CustomerSearchForm()

    if request.method == 'POST':
        return search_results(search)

    return render_template('search_customers.html', form=search)    


@app.route('/results')
@login_required
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search_string:
        if search.data['select'] == 'first_name':
            qry = db.session.query(Customer).filter(
                Customer.first_name.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'last_name':
            qry = db.session.query(Customer).filter(
                Customer.last_name.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'email':
            qry = db.session.query(Customer).filter(
                Customer.email.contains(search_string))
            results = qry.all()
        else:
            qry = db.session.query(Customer)
            results = qry.all()
    else:
        qry = db.session.query(Customer)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect(url_for('search_customers'))
    else:
        # display results
        table = CustomerResults(results)
        table.border = True
        return render_template('results.html', table=table)

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

@app.route('/success/')
@login_required
def success():
    return render_template('/success.html')      

# Tables
class CustomerResults(Table):
    id = Col('Id', show=False)
    first_name = Col('First Name')
    last_name = Col('Last Name')
    email = Col('Email')
    phone = Col('Phone')
    