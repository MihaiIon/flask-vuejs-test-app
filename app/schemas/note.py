from flask_restx import fields
from app.api import api_rest

create_note_model = api_rest.model('Note', {
    'title': fields.String(required=True, description='Note title'),
    'content': fields.String(required=True, description='Note content'),
    'author_full_name': fields.String(default='Anonymous')
})
