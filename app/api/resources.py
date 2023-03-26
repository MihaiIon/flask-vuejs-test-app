"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from flask import request
from flask_restx import Resource, abort
from . import api_rest

from app.repositories import AuthorRepository, NoteRepository
from app.schemas import *
from .parsers import *

@api_rest.route('/author/')
class Author(Resource):
    @api_rest.marshal_with(author_model_schema)
    def post(self):
        args = author_reqparser.parse_args()

        author_repository = AuthorRepository()
        new_author = author_repository.create_author(first_name=args['first_name'], last_name=args['last_name'])

        return new_author

@api_rest.route('/note/')
class Note(Resource):
    @api_rest.marshal_with(note_model_schema)
    def post(self):
        args = note_reqparser.parse_args()

        note_repository = NoteRepository()
        new_note = note_repository.create_note(title=args['title'], content=args['content'])

        return new_note
