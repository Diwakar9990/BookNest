from marshmallow import fields, Schema

class RatingSchema(Schema):
    id = fields.Integer()
    rating = fields.Integer()
    user_id = fields.Integer()
    book_id = fields.Integer()
    feedback = fields.String()