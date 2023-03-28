from flask_restx import reqparse

def non_empty_string(s):
    if not s or not s.strip():
        raise ValueError("Must not be empty string")
    return s

author_reqparser = reqparse.RequestParser()
author_reqparser.add_argument('first_name', type=non_empty_string, required=True, help='An author must have first name  |')
author_reqparser.add_argument('last_name', type=non_empty_string, required=True, help='An author must have last name  |')

create_note_reqparser = reqparse.RequestParser()
create_note_reqparser.add_argument('title', type=str, required=True, help='A note must have a title |')
create_note_reqparser.add_argument('content', type=str, required=True, help='A note must have a content |')
create_note_reqparser.add_argument('author_id', type=int)

update_note_reqparser = reqparse.RequestParser()
update_note_reqparser.add_argument('title', type=non_empty_string, help='A note must have a title |')
update_note_reqparser.add_argument('content', type=non_empty_string, help='A note must have a content |')
update_note_reqparser.add_argument('author_id', type=int)
