#!usr/bin/python
from flask.ext.wtf import Form #imports form class.
from wtforms import StringField, BooleanField #imports field classes
from wtforms.validators import DataRequired #ensures field is not submitted empty

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

