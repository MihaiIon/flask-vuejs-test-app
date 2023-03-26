from flask_restx import reqparse

note_parser = reqparse.RequestParser()
note_parser.add_argument('title', type=str, required=True, help='A note must have a title |')
note_parser.add_argument('content', type=str, required=True, help='A note must have a content |')
note_parser.add_argument('author_id', type=int)
