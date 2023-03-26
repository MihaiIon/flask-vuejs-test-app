from app.models import NoteModel

from app.utils import Database
db = Database.instance()

class NoteRepository:
    def create_note(self, title: str, content: str):
        note = NoteModel(title=title, content=content)
        db.session.add(note)
        db.session.commit()
        return note
