from flask import Flask
from flask_cors import CORS

#Creating a Flask instance
app = Flask(__name__) 
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:8080"}})
#setup the Configurations
app.config.from_prefixed_env()
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

#user @/api/users
from user.user_routes import user_bp
app.register_blueprint(user_bp, url_prefix='/api/users')

#library @/api/section
from library.section_routes import section_bp
app.register_blueprint(section_bp, url_prefix='/api/sections')

#library @/api/books    
from library.book_routes import book_bp
app.register_blueprint(book_bp, url_prefix='/api/books')

#request @/api/requests
from request.request_routes import request_bp
app.register_blueprint(request_bp, url_prefix='/api/requests')

#ratings @/api/ratings
from ratings.ratings_routes import ratings_bp
app.register_blueprint(ratings_bp, url_prefix='/api/ratings')

import user.user_model

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=5000))