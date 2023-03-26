from datetime import datetime
from . import AuthorModel

from app.utils import Database
db = Database.instance()

class NoteModel(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship(AuthorModel, backref='notes')
