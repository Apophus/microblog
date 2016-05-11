#!usr/bin/python

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])#methods argument tells flask that the view accepts GET and POST requests 
def login():
    form = LoginForm()
    if form.validate_on_submit():#this function does all the processing work.If form gets submitted before it's filled, it returns False.
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))#if validate_on_submit returns true flash displays message on next page to user.
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
