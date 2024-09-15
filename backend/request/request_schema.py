from marshmallow import fields, Schema

class RequestSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    book_id = fields.Integer()
    request_date = fields.DateTime()
    status = fields.String()