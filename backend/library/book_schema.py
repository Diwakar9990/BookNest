from marshmallow import fields, Schema

class BookSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    author = fields.String()
    status = fields.Boolean()
    content = fields.String()
    section_id = fields.Integer()
    ebook_url =  fields.String()

    