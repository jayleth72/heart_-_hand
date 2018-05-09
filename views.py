from app import app
from flask_security import login_required
from flask import render_template
from flask_wtf import FlaskForm
from forms import *

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
    form = CustomerEntryForm()
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