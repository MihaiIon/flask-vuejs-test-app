"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from flask import request
from flask_restx import Resource, abort
from . import api_rest

from app.models import NoteModel
from app.repositories import NoteRepository
from app.schemas.note import note_model
from .parsers import note_parser

from app.utils import Database
db = Database.instance()

@api_rest.route('/note/')
class Note(Resource):
    @api_rest.marshal_with(note_model)
    def post(self):
        args = note_parser.parse_args()
        title = args.get('title')
        content = args.get('content')

        note_repository = NoteRepository()
        new_note = note_repository.create_note(title=title, content=content)

        return new_note
