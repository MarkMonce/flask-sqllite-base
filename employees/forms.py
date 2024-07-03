

from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField,StringField,SubmitField, DateField, DateTimeField, TimeField
from wtforms.validators import DataRequired, Length

class EmployeeForm(FlaskForm):

    firstname = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    address1 = StringField('Address 1', validators=[DataRequired(), Length(max=50)])
    address2 = StringField('Address 2')
    city = StringField('City', validators=[DataRequired(), Length(max=20)])
    state = StringField('State', validators=[DataRequired(), Length(max=2)])
    zip = StringField('ZIP Code', validators=[DataRequired(), Length(min=5, max=5)])
    hourlyrate = FloatField('Hourly Rate', validators=[DataRequired()])
    age = IntegerField('Age', validators=[])
    submit = SubmitField('Submit')