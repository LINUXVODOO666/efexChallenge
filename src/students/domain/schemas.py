from marshmallow import Schema,fields

class SchemaStudent(Schema):
    first_name=fields.String(required=True,allow_none=False)
    last_name=fields.String(required=True,allow_none=False)
    date_of_birth=fields.Date(required=True,allow_none=False)
    grade=fields.Integer(required=True,allow_none=False)
    phone=fields.String(required=True,allow_none=False)
    email=fields.Email(required=True,allow_none=False)


class SchemaStudentUpdate(Schema):
    first_name=fields.String(required=False,allow_none=False)
    last_name=fields.String(required=False,allow_none=False)
    date_of_birth=fields.Date(required=False,allow_none=False)
    grade=fields.Integer(required=False,allow_none=False)
    phone=fields.String(required=False,allow_none=False)
    email=fields.Email(required=False,allow_none=False)