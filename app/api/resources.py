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
    @api_rest.marshal_with(author_model)
    def post(self):
        args = author_reqparser.parse_args()

        author_repository = AuthorRepository()
        new_author = author_repository.create_author(first_name=args['first_name'], last_name=args['last_name'])

        return new_author

@api_rest.route('/note/')
class Note(Resource):
    @api_rest.marshal_with(note_model)
    def post(self):
        args = note_reqparser.parse_args()

        note_repository = NoteRepository()
        new_note = note_repository.create_note(attributes_to_update=args)

        return new_note

    @api_rest.marshal_with(note_model)
    def put(self):
        args = update_note_reqparser.parse_args()
        print(args)
        note_repository = NoteRepository()
        modified_note = note_repository.update_note(note_id=args['id'], attributes_to_update=args)

        return modified_note
