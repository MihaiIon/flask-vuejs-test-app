import os
import pytest

from app import app, db
from sqlalchemy.sql import text

# define test database URI
TEST_DB_URI = 'sqlite:///flask_vuejs_test_app.db'

# configure app for testing
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI

# define schema path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)  # get the parent directory of the current folder
SQL_SCHEMA_PATH = os.path.join(ROOT_DIR, 'schema.sql') 

@pytest.fixture(scope='module')
def client():
    # bind app to new test database
    with app.test_client() as client:        
        with app.app_context():
            db.create_all()

            # create database from schema
            with open(SQL_SCHEMA_PATH) as f:
                queries = f.read().split(';')
                for query in queries:
                    db.session.execute(text(query + ';'))
            db.session.commit()

            yield client

            # close the database connection and remove the test database
            db.session.remove()
            db.drop_all()
