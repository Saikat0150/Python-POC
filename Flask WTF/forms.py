from flask_wtf import Form
from wtforms import *


class ContactForm(Form):
    name = TextField("Candidate Name ", [validators.Required("Please enter your name.")])
    Gender = RadioField("Gender", choices = [('M','Male'),('F', 'Female')])
    Address = TextAreaField("Address")
    email = TextField("Email", [validators.Required("Please enter your email address.")])
    Age = IntegerField("Age")
    language = SelectField('Programming Languages', choices=[('java', 'java'), ('py','Python')])
    submit = SubmitField("Submit")
    