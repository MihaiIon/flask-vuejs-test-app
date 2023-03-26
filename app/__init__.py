import os
from flask import Flask, current_app, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../dist/static')

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

# initialize database connection
from app.utils import Database
if os.environ.get('TESTING') == 'True':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_vuejs_dev_app.db'

Database(app)

# TODO
from .api import api_bp
from .client import client_bp

app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

# TODO 
@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
