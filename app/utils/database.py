from flask_sqlalchemy import SQLAlchemy

class Database(object):
    _instance = None
    _db = None

    def __new__(cls, app):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._db = SQLAlchemy(app)

        return cls._instance

    @classmethod
    def instance(cls):
        if cls._db is None:
            raise Exception('Database not initialized')

        return cls._db
