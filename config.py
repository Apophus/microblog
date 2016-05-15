#!usr/bin/python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')#path to the database
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')#folder where SQLAlchemy-migrate files are stored.
