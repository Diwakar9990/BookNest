from main import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy(app)

from request.request_model import Request
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True ,nullable=False)
    password = db.Column(db.Text())
    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

from library.section_model import Section
from library.book_model import Book
from ratings.ratings_model import Rating


with app.app_context():
    db.create_all()
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin', 
            email='admin123@gmail.com',
        )
        admin.set_password('admin1234')
        admin.save()
 