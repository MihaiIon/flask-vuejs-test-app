from app.models import NoteModel

from app.utils import Database
db = Database.instance()

class NoteRepository:
    def create_note(self, title: str, content: str, author_id: int):
        note = NoteModel(title=title, content=content)

        note.author_id = author_id if author_id else None

        db.session.add(note)
        db.session.commit()
        
        return note
