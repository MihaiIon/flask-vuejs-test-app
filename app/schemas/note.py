from flask_restx import fields
from app.api import api_rest

note_model = api_rest.model('Note', {
    'id': fields.Integer(readOnly=True, description='Note identifier'),
    'title': fields.String(required=True, description='Note title'),
    'content': fields.String(required=True, description='Note content'),
    'author_full_name': fields.String(default='Anonymous')
})
