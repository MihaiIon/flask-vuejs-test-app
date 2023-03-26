from flask_restx import fields
from app.api import api_rest

def format_author_full_name(author):
    return f"{author.first_name} {author.last_name}"

author_model = api_rest.model('Author', {
    'id': fields.Integer(readOnly=True, description='Author identifier'),
    'first_name': fields.String(required=True, description='Author first name'),
    'last_name': fields.String(required=True, description='Author last name'),
    'full_name': fields.String(attribute=format_author_full_name)
})

note_model = api_rest.model('Note', {
    'id': fields.Integer(readOnly=True, description='Note identifier'),
    'title': fields.String(required=True, description='Note title'),
    'content': fields.String(required=True, description='Note content'),
    'author_full_name': fields.String(attribute=lambda note: format_author_full_name(note.author) if note.author else 'Anonymous')
})
