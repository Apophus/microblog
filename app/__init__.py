#!usr/bin/python
from flask import Flask
'''Created an application object called **app** of class **Flask**
'''
app = Flask(__name__) #app is the variable assigned to the Flask instance
'''The import Statement is not at the start of the script as is the norm reason being we are trying to avoid **Circular references**
The views module needs to import the app variable defined in this script
So.. Putting it down here helps avoid  **circular import errors**'''
from app import views #app is the package that from which we import the                          ** views module**


