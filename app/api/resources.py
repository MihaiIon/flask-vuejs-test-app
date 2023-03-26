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
from app.schemas.note import note_model

import pytest

from app.utils import Database
db = Database.instance()

@api_rest.route('/note/')
class Note(Resource):

    @api_rest.marshal_with(note_model)
    def post(self):
        title = request.form.get('title')
        abort(400, message='A note must have a title') if not title else None
        
        content = request.form.get('content')
        abort(400, message='A note must have a content') if not content else None

        new_note = NoteModel(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()

        return new_note
