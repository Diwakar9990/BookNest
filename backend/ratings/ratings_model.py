from user.user_model import db

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer(), primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    book_id = db.Column(db.Integer(), db.ForeignKey('books.id'))
    feedback = db.Column(db.String(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()