from marshmallow import fields, Schema

class SectionSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    date_Created = fields.DateTime()