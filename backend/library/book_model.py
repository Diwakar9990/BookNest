book_list = [
    {
        "author": "author",
        "content": "book 1 content",
        "id": 0,
        "section": "book 1 section",
        "status": "requested",
        "title": "book 1"
    },
    {
        "author": "author 2",
        "content": "book 2 content",
        "id": 1,
        "section": 1,
        "status": "requested",
        "title": "book 2"
    },
    {
        "author": "author 3",
        "content": "book 3 content",
        "id": 2,
        "section": 0,
        "status": "requested",
        "title": "book 3"
    },
    {
        "author": "author 4",
        "content": "book 4 content",
        "id": 3,
        "section": 0,
        "status": "requested",
        "title": "book 4"
    },
    {
        "author": "author 5",
        "content": "book 5 content",
        "id": 4,
        "section": 0,
        "status": "requested",
        "title": "book 5"
    }
]

from user.user_model import db

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    author = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=True)
    ebook_url = db.Column(db.String(255), nullable=True)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))
    ratings = db.relationship('Rating', backref='book')
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()