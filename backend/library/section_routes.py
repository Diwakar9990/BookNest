from main import app
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, request
from library.section_model import Section_list
from library.section_model import Section
from library.section_schema import SectionSchema
from datetime import datetime

section_bp = Blueprint('section', __name__)

# Get all sections
@section_bp.get('/')
@jwt_required()
def get_all_section(): 
    sections = Section.query.all()
    if (sections):
        result = SectionSchema().dump(sections, many=True)
        resp = jsonify({
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
        'error': 'Nothing Found'
    }), 404

# add a section
@section_bp.post('/')
@jwt_required()
def add_section():
    data = request.get_json()
    print(data)
    name = data['name']
    section = Section.query.filter_by(name = name).first()
    print(section)
    if section is not None:
        resp = jsonify({
            "message": "section already exists",
        })
        return resp, 401
    else:
        new_section = Section(
            name = data.get('name'),
            description = data.get('description'),
        )
        new_section.save()
        result = SectionSchema().dump(new_section, many=False)
        resp = jsonify({
            "message": "section created successfully",
            "res": result,
        })
        return resp, 201


# get section by id
@section_bp.get('/<int:id>')
@jwt_required()
def get_one_section(id):
    section = Section.query.get(id)
    if(section):
        result = SectionSchema().dump(section, many=False)
        resp = jsonify({
            "res": result,
        })
        return resp, 200
    else: 
        return jsonify({
            'error': 'Nothing Found'
        }), 404

# update section by id
@section_bp.put('/<int:id>')
@jwt_required()
def update_section(id):
    data = request.get_json()
    section = Section.query.get(id)
    if section:
        section.name = data.get('name')
        section.description = data.get('description')
        section.save()
        result = SectionSchema().dump(section, many=False)
        resp = jsonify({
            "message": "section updated successfully",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
            'error': 'Section Not Found'
        }), 404

# delete section by id
@section_bp.delete('/<int:id>')
@jwt_required()
def delete_section(id):
    section = Section.query.filter_by(id=int(id)).first()
    if section:
        section.delete()
        result = SectionSchema().dump(section, many=False)
        resp = jsonify({
            "message": "section Deleted successfully",
            "res": result,
        })
        return resp, 200
    else:
        return jsonify({
            'error': 'Section Not Found'
        }), 404


