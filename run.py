#!flask/bin/python
'''THis script starts the development web server with our application'''
from app import app #imports the app variable from the app package which holds the Flask instance
app.run(debug=True) #invokes the run method to start the server.
