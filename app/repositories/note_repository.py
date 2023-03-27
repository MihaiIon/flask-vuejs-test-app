from app.models import NoteModel as Model

from app.utils import Database
db = Database.instance()

class NoteRepository:
    def create_note(self, attributes_to_update):
        attrs = attributes_to_update
        record = Model(title=attrs['title'], content=attrs['content'])

        record.author_id = attrs['author_id'] if attrs['author_id'] else None

        db.session.add(record)
        db.session.commit()
        return record

    def update_note(self, note_id: int, attributes_to_update):
        attrs = attributes_to_update
        record = db.session.get(Model, note_id)

        if attrs['title']:
            record.title = attrs['title']

        if attrs['content']:
            record.content = attrs['content']

        record.author_id = attrs['author_id']

        db.session.commit()
        return record
