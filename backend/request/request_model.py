from sqlalchemy import Enum
from datetime import datetime
now = datetime.utcnow
import enum
request_list = [
    {
        'id': 0,
        'username': 'username',
        'book_id': 0,
        'req_date': '16/06/24',
        'status': 'REQUESTED',        
    }
]

from user.user_model import db

class RequestType(enum.Enum):
    REQUESTED = "requested"
    ISSUED = "issued"
    RETURNED = "returned"

class Request(db.Model):
    __tablename__ = 'requests'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.DateTime, default=now)
    status = db.Column(db.String, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()