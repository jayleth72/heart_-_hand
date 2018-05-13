from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField

class CustomerEntryForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired())
    last_name = StringField('Last Name', validators=[DataRequired())
    email = StringField('Email', validators=[DataRequired())
    street_address = StringField('Street Address', validators=[DataRequired())
    suburb = StringField('Suburb', validators=[DataRequired())
    state = SelectField(u'State', choices=[('QLD', 'Queensland'), ('NT', 'Northern Territory'), ('WA', 'Western Australia'), ('NSW', 'New South Wales'), ('Vic', 'Victoria'), ('Tas', 'Tasmania'), ('SA', 'South Australia')])
    postcode = IntegerField('Postcode', validators=[DataRequired())
    phone = StringField('Phone', validators=[DataRequired())
    alternative_contact = StringField('Alternative Contact')
    alternative_contact_phone = StringField('Alternative Contact Phone')
    notes = StringField('Notes')

    