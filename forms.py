from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired

class CustomerEntryForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message='First name is required')])
    last_name = StringField('Last Name', validators=[InputRequired(message='Last name is required')])
    email = EmailField('Email', validators=[InputRequired(message='Email is required')])
    street_address = StringField('Street Address', validators=[InputRequired(message='Street address is required')])
    suburb = StringField('Suburb', validators=[InputRequired(message='Suburb is required')])
    state = SelectField(u'State', choices=[('QLD', 'Queensland'), ('NT', 'Northern Territory'), ('WA', 'Western Australia'), ('NSW', 'New South Wales'), ('Vic', 'Victoria'), ('Tas', 'Tasmania'), ('SA', 'South Australia')])
    postcode = IntegerField('Postcode', validators=[InputRequired(message='Postcode is required')])
    phone = StringField('Phone', validators=[InputRequired(message='Phone No. is required')])
    alternative_contact = StringField('Alternative Contact')
    alternative_contact_phone = StringField('Alternative Contact Phone')
    notes = TextAreaField('Notes')

class CustomerSearchForm(FlaskForm):
    choices = [('first_name', 'First name'), ('last_name', 'Last name'), ('email', 'email') ]
    select = SelectField('Search for Customers:', choices=choices)
    search = StringField('')    

class ChildEntryForm(FlaskForm):
    parent_id = IntegerField('parent_id')
    first_name = StringField('First Name', validators=[InputRequired(message='First name is required')])
    last_name = StringField('Last Name', validators=[InputRequired(message='Last name is required')])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired(message='Date of birth is required')])
    notes = TextAreaField('Notes')    