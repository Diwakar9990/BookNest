from main import app
from library.book_model import book_list
from request.request_model import request_list, Request
from request.request_schema import RequestSchema
from user.user_schema import UserSchema
from library.book_model import Book
from user.user_model import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from datetime import datetime

request_bp = Blueprint('req', __name__)

# librarian will get all pending requests
@request_bp.get('/get-pending-requests')
@jwt_required()
def get_pending_requests():
    username = get_jwt_identity()
    if username == 'admin':
        pending_requests = Request.query.filter_by(status='REQUESTED').all()
        if pending_requests:
            result = RequestSchema().dump(pending_requests, many=True)
            resp = jsonify({
                "message": f'All pending requests',
                "res": result,
            })
            return resp, 200
        else:
            return jsonify({
                'msg': 'No pending requests'
            }), 403
    else:
        return jsonify({
            'msg': 'You are not authorized to view this request'
        }), 401
       
# librarian will get all pending requests
@request_bp.get('/get-granted-requests')
@jwt_required()
def get_granted_requests():
    username = get_jwt_identity()
    if username == 'admin':
        pending_requests = Request.query.filter_by(status='APPROVED').all()
        if pending_requests:
            result = RequestSchema().dump(pending_requests, many=True)
            resp = jsonify({
                "message": f'All Granted requests',
                "res": result,
            })
            return resp, 200
        else:
            return jsonify({
                'msg': 'No Granted requests'
            }), 403
    else:
        return jsonify({
            'msg': 'You are not authorized to view this request'
        }), 401

# get all book requests by user 
@request_bp.get('/user-request-details')
@jwt_required()
def get_all_requests_details_of_user():
    username = get_jwt_identity()
    user_requests_count = Request.query.filter_by(username=username).count()
    pending_request_count = Request.query.filter_by(username=username, status="REQUESTED").count()
    accepted_request_count = Request.query.filter_by(username=username, status="APPROVED").count()
    rejected_request_count = Request.query.filter_by(username=username, status="REJECTED").count()
    result = {
        'total_request': user_requests_count,
        'pending_request': pending_request_count,
        'accepted_request': accepted_request_count,
        'rejected_request': rejected_request_count,
    }
    return jsonify({
        'result' : result,
    }), 200

# get all book requests by user 
@request_bp.get('/user')
@jwt_required()
def get_all_requests_by_user():
    username = get_jwt_identity()
    user_requests = Request.query.filter_by(username=username).all()
    if user_requests:
        result = RequestSchema().dump(user_requests, many=True)
        resp = jsonify({
            "message": f'All requests by {username}',
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
            'error': 'No request was made'
        }), 404

# creates a new request
@request_bp.get('/new/<int:book_id>')
@jwt_required()
def add_request(book_id):
    bookId = book_id
    username = get_jwt_identity()
    user_request = Request.query.filter_by(username=username, book_id=bookId).first()
    if user_request:
        resp = jsonify({
            "message": "You have already requested for this book",
        })
        return resp, 401
    
    requests = Request.query.filter_by(username=username, status="REQUESTED").all()
    results = RequestSchema().dump(requests, many=True)
    if len(results) < 5:
        status = 'REQUESTED'
        new_request = Request(
            username = username,
            book_id = bookId,
            status = status
        )
        new_request.save()
        result = RequestSchema().dump(new_request, many=False)
        resp = jsonify({
            "message": "Request created successfully",
            "res": result,
        })
        return resp, 201
    else:
        resp = jsonify({
                "message": "You cannot request more than 5 books",
            })
        return resp, 200

# updates request by librarian
@request_bp.put('/update/<int:id>')
@jwt_required()
def update_request(id):
    username = get_jwt_identity()
    data = request.get_json()
    action = data['action']
    if action == 'approve':
        status = 'APPROVED'
    elif action == 'reject':
        status = 'REJECTED'
    else:
        return jsonify({
            'error': 'Invalid Response'
        }), 400
    
    if username == 'admin':
        user_request = Request.query.get(id)
        user_request.status = status
        user_request.save()
        result = RequestSchema().dump(user_request, many=False)
        resp = jsonify({
            "message": "Request updated successfully",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
            'error': 'You are not authorized to update this request',
        }), 401

# delete request
@request_bp.delete('/delete/<int:id>')
@jwt_required()
def delete_request(id):
    user_request = Request.query.get(id)
    if user_request:
        user_request.delete()
        result = RequestSchema().dump(user_request, many=False)
        resp = jsonify({
            "message": "Request Deleted successfully",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
            'error': 'No request found for id ' + id
        }), 404
