from main import app
from ratings.ratings_model import Rating
from ratings.ratings_schema import RatingSchema
from user.user_model import User
from user.user_schema import UserSchema
from library.book_model import Book
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from datetime import datetime

ratings_bp = Blueprint('rating', __name__)

# get the average_rating for a book 
@ratings_bp.get('/average/<int:bookId>')
@jwt_required()
def average_rating(bookId):
    ratings = Rating.query.filter_by(book_id=bookId).all()
    if ratings:
        result = RatingSchema().dump(ratings, many=True)
        total = 0
        for rts in result:
            total += rts['rating']
        ratingCount = len(result)
        average_rating = float(total/ratingCount)
        average_rating = round(average_rating,2)
        resp = jsonify({
                "message": f'average ratings of the book',
                "rating": average_rating,
                "ratingCount": ratingCount
            })
        return resp, 200
    else:
        return jsonify({
            'msg': 'No one rated yet',
        }), 200

# get all the ratings of the book
@ratings_bp.get('/<int:bookId>')
@jwt_required()
def get_ratings(bookId):
    ratings = Rating.query.filter_by(book_id=bookId).all()
    if ratings:
        result = RatingSchema().dump(ratings, many=True)
        resp = jsonify({
                "message": f'ratings of the book id {bookId}',
                "res": result,
            })
        return resp, 200
    else:
        return jsonify({
            'msg': 'Be the first One to rate this book'
        }), 404

# add rating to a book 
@ratings_bp.post('/<int:bookId>')
@jwt_required()
def add_rating(bookId):
    data = request.get_json()
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    user_result = UserSchema().dump(user, many=False)
    userId = user_result['id']
    book = Book.query.filter_by(id=bookId).first()
    rate = data['rate']
    feedback = data['feedback']
    existing_rating = Rating.query.filter_by(user_id=userId, book_id=bookId).first()
    if existing_rating:
        return jsonify({
            'msg': 'You have already rated this book'
        }), 401
    else:
        if rate > 0 and rate <= 5:
            new_rating = Rating(
                rating = rate,
                user_id = userId,
                book = book,
                feedback = feedback
            )
            new_rating.save()
            result = RatingSchema().dump(new_rating, many=False)
            resp = jsonify({
                    "message": 'Rating added successfully',
                    "res": result,
                })
            return resp, 201
        else:
            return jsonify({
            'msg': 'rate only between 1 to 5'
        }), 401

# #  delete a rating
# @ratings_bp.delete('/<int:id>')
# @jwt_required
# def delete_rating(id):
#     ratings = Rating.query.get(id)
#     if ratings:
#         result = RatingSchema.dump(ratings, many=False)
#         ratings.delete()
#         resp = jsonify({
#                 "message": 'Rating deleted successfully',
#                 "res": result,
#             })
#         return resp, 200
#     else:
#         return jsonify({
#             'msg': 'Rating not found',
#         }), 404
    





        