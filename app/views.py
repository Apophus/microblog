#!usr/bin/python

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])#methods argument tells flask that the view accepts GET and POST requests 
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
