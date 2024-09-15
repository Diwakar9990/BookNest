from datetime import datetime
now = datetime.utcnow

Section_list = [
    {
        "id": 0,
        "name": "History",
        "dateCreated": datetime.now(),
        "books": [2,3,4],
        "Description": "This category contains information about the history"
    },
    {
        "id": 1,
        "name": "Science",
        "dateCreated": datetime.now(),
        "books": [1],
        "Description": "This category contains information about the Science"
    },
    {
        "id": 2,
        "name": "Horror",
        "dateCreated": datetime.now(),
        "books": [],
        "Description": "This category contains information about the Horror"
    },
]

from user.user_model import db;

class Section(db.Model):
    __tablename__ = 'sections'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date_Created = db.Column(db.DateTime, default=now)
    description = db.Column(db.Text)
    books = db.relationship('Book', backref='section')

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()