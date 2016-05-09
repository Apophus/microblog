#!usr/bin/python
'''
This is the configuration settings.
Flask WTF extension wraps the WTForms in a way that intergrate nicely with flask app.
**WTF_CSFR_ENABLED** activates cross-site forgery request prevention which makes the site more secure.
SECRET_KEY is only needed where CSFR  is enabled. It provides a cryptographic token used to validate web forms. 
'''
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

