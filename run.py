import os
from app import app
from app.utils import Database

# Allow cross-origin requests from any domain
from flask_cors import CORS
CORS(app)

# Initialize the database
db = Database.instance()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SQL_SCHEMA_PATH = os.path.join(ROOT_DIR, 'schema.sql')
DATABASE_PATH = os.path.join(ROOT_DIR, 'instance/flask_vuejs_dev_app.db')

# Create database with schema (if it does not exist)
from sqlalchemy.sql import text

if not os.path.exists(DATABASE_PATH):
    with app.app_context():
        db.create_all()
        with open(SQL_SCHEMA_PATH) as f:
            queries = f.read().split(';')
            for query in queries:
                db.session.execute(text(query + ';'))
        db.session.commit()

# Launch app
app.run(port=8000, debug=True)
