import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')#required by Flask-SQLAlchemy extension. It's the path to the database file.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')#SQLALCHEMY_MIGRATE_REPO is the folder where we store the SQLAllchemy-migrate data files.
