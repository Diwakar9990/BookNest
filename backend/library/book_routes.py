from main import app, cors
from flask import send_from_directory
from library.book_model import book_list
from library.book_model import Book
from request.request_model import Request
from library.book_schema import BookSchema
from library.section_model import Section
from library.section_model import Section_list
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from user.user_model import db
from ratings.ratings_model import Rating
from user.user_model import User
import os

book_bp = Blueprint('book', __name__)
cors

# Ensure your app is configured to handle file uploads
UPLOAD_FOLDER = 'static/ebooks'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@book_bp.get('/download/<filename>')
@jwt_required()
def download_file(filename):
    try:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename,
            as_attachment=True
        )
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

# add new book to database
@book_bp.post('/')
@jwt_required()
def add_book():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        ebook_url = filename

        data = request.form  
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')
        section_name = data.get('section')
        section = Section.query.filter_by(name=section_name).first()
        new_book = Book(
            title=title,
            content=content,
            author=author,
            section=section,
            ebook_url=ebook_url
        )
        new_book.save()
        result = BookSchema().dump(new_book, many=False)
        resp = jsonify({
            "message": "Book added successfully",
            "res": result,
        })
        return resp, 201


# get all books from the database
@book_bp.get('/')
@jwt_required()
def get_all_books():
    books = Book.query.all()
    if books:
        result = BookSchema().dump(books, many=True)
        resp = jsonify({
            "message": "list of all books",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
        'error': 'Nothing Found'
    }), 404


# get a book by id
@book_bp.get('/<int:id>')
@jwt_required()
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({
            'error': 'Book not found',
        }), 404
    else:
        result = BookSchema().dump(book, many=False)
        resp = jsonify({
            "res": result,
            })
        return resp, 200
    
# update book by id
@book_bp.put('/<int:id>')
@jwt_required()
def update_book(id):
    data = request.get_json()
    title = data['title']
    content = data['content']
    author = data['author']
    section_name = data['section']
    section = Section.query.filter_by(name=section_name).first()
    book = Book.query.get(id)
    if book is None:
        return jsonify({
            'error': 'book Not Found'
        }), 404
    else:       
        book.title = title
        book.content = content
        book.author = author
        book.section = section
        book.save()
        result = BookSchema().dump(book, many=False)
        resp = jsonify({
            "message": "Book updated successfully",
            "res": result,
        })
        return resp, 200

# delete book by id
@book_bp.delete('/<int:id>')
@jwt_required()
def delete_book(id):
    book = Book.query.get(id)
    if book is None:    
        return jsonify({
            'error': 'Book Not Found'
        }), 404
    else:
        book.delete()
        result = BookSchema().dump(book, many=False)
        resp = jsonify({
            "message": "Book deleted successfully",
            "res": result,
        })
        return resp, 200


# get books by section id
@book_bp.get('/section/<int:section_id>')
@jwt_required()
def get_books_by_section(section_id):
    books = Book.query.filter_by(section_id=section_id).all()
    if books:
        result = BookSchema().dump(books, many=True)
        resp = jsonify({
            "message": f'books filtered by section id {section_id}',
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({'msg':'No books are added in this section'}), 404
    
# get books by request status as accepted
@book_bp.get('/request-status-accepted')
@jwt_required()
def get_accepted_books():
    username = get_jwt_identity()
    accepted_requests = Request.query.filter_by(username=username, status='APPROVED').all()
    if accepted_requests:
        book_ids = [request.book_id for request in accepted_requests]
        books = Book.query.filter(Book.id.in_(book_ids)).all()
        if books:
            result = BookSchema().dump(books, many=True)
            resp = jsonify({
                "message": "list of books with approved requests",
                "res": result,
            })
            return resp, 200
        else:
            return jsonify({'msg': 'No books found for approved requests'}), 404
    else:
        return jsonify({'msg': 'No approved requests found'}), 404

# search books by author, section, or name
@book_bp.post('/search')
@jwt_required()
def search_books():
    data = request.get_json()
    author = data.get('author')
    section_name = data.get('section')
    title = data.get('title')
    
    query = Book.query
    
    if author:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    if section_name:
        section = Section.query.filter_by(name=section_name).first()
        if section:
            query = query.filter_by(section_id=section.id)
        else:
            return jsonify({'msg': 'No section found with the given name'}), 404
    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    
    books = query.all()
    
    if books:
        result = BookSchema().dump(books, many=True)
        resp = jsonify({
            "message": "list of books matching search criteria",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({'msg': 'No books found matching search criteria'}), 404
    
@book_bp.get('/section_counts')
@jwt_required()
def get_number_of_books_by_section():
    sections = Section.query.all()
    if not sections:
        return jsonify({'msg': 'No sections found'}), 404

    section_counts = []
    section_labels = []

    for section in sections:
        book_count = Book.query.filter_by(section_id=section.id).count()
        section_labels.append(section.name)
        section_counts.append(book_count)

    result = {
        'labels': section_labels,
        'counts': section_counts
    }

    return jsonify({
        "message": "Book counts by section",
        "res": result,
    }), 200

@book_bp.get('/most_rated')
@jwt_required()
def get_most_rated_books():
    # Query to get books with the most ratings
    most_rated_books = db.session.query(
        Book.title,
        db.func.count(Rating.id).label('rating_count')
    ).join(Rating).group_by(Book.id).order_by(db.desc('rating_count')).limit(10).all()

    if not most_rated_books:
        return jsonify({'msg': 'No ratings found'}), 404

    book_titles = [book[0] for book in most_rated_books]
    rating_counts = [book[1] for book in most_rated_books]

    result = {
        'titles': book_titles,
        'counts': rating_counts
    }

    return jsonify({
        "message": "Most rated books",
        "res": result,
    }), 200

@book_bp.get('/stats')
@jwt_required()
def get_counts():
    # Count the total number of books
    total_books = Book.query.count()

    # Count the total number of users
    total_users = User.query.count()
    total_users = total_users - 1

    # Count the total number of sections
    total_sections = Section.query.count()

    # Count the total number of requests in different states
    total_requests = Request.query.count()
    pending_requests = Request.query.filter_by(status='REQUESTED').count()
    accepted_requests = Request.query.filter_by(status='APPROVED').count()
    rejected_requests = Request.query.filter_by(status='REJECTED').count()

    # Return all counts as a JSON response
    return jsonify({
        'total_books': total_books,
        'total_users': total_users,
        'total_sections': total_sections,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'accepted_requests': accepted_requests,
        'rejected_requests': rejected_requests,
    }), 200