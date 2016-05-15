#!usr/bin/python
'''
This is the configuration settings.
Flask WTF extension wraps the WTForms in a way that intergrate nicely with flask app.
**WTF_CSFR_ENABLED** activates cross-site forgery request prevention which makes the site more secure.
SECRET_KEY is only needed where CSFR  is enabled. It provides a cryptographic token used to validate web forms. 
'''
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
