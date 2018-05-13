from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField

class CustomerEntryForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    email = StringField('email')
    street_address = StringField('first_name')
    suburb = StringField('first_name')
    state = SelectField(u'State', choices=[('WA', 'Western Australia'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('NSW', 'New South Wales'), ('Vic', 'Victoria'), ('Tas', 'Tasmania'), ('SA', 'South Australia')])
    postcode = IntegerField('postcode')
    phone = StringField('phone')
    alternative_contact = StringField('alternative_contact')
    alternative_contact_phone = StringField('alternative_contact_phone')
    notes = StringField('notes')