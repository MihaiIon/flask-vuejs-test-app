from flask_restx import reqparse

author_reqparser = reqparse.RequestParser()
author_reqparser.add_argument('first_name', type=str, required=True, help='An author must have first name  |')
author_reqparser.add_argument('last_name', type=str, required=True, help='An author must have last name  |')

note_reqparser = reqparse.RequestParser()
note_reqparser.add_argument('title', type=str, required=True, help='A note must have a title |')
note_reqparser.add_argument('content', type=str, required=True, help='A note must have a content |')
note_reqparser.add_argument('author_id', type=int)
