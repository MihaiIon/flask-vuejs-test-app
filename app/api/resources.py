"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

# from datetime import datetime
from flask import request
from flask_restx import Resource, abort
from flask_sqlalchemy import SQLAlchemy

# from .security import require_auth
from . import api_rest
from app.models import NoteModel
from app.schemas.note import create_note_model

import pytest

from app.utils import Database
db = Database.instance()


