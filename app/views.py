#!usr/bin/python
'''
**Views** are handlers that respond to requests from browsers and other clients.
In Flask they are written as python functions
Each is mapped to one or more **REQUEST URLs**

    The view we are creating returns a string to be displayed on the client's web browser
'''
from app import app
'''Essentially, decorators work as wrappers, modifying the behavior of the code before and after a target function execution.

These decorators create mappings from _URLs_ / and _/index_ to it's function
'''
@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
