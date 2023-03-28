from app.models import AuthorModel as Model

from app.utils import Database
db = Database.instance()

class AuthorRepository:
    def all(self):
        records = db.session.query(Model).all()
        return records

    def create_author(self, first_name: str, last_name: str):
        record = Model(first_name=first_name, last_name=last_name)
        db.session.add(record)
        db.session.commit()
        return record