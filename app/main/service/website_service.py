import datetime

from app.main import db
from app.main.model.website import Website
from typing import Dict, Tuple
import json

def save_new_website(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    website = Website.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'fail',
        'message': 'Website already exists.'
    }
    response_code = 409

    if not website:
        new_website = Website(
            website=data['website'],
            username=data['username'],
            resume_date=data['resume_date'],
            cover_letter_date=data['cover_letter_date'],
            comments=data['comments']
        )
        save_changes(new_website)
        response_object = {
            'status': 'success',
            'message': 'Website successfully saved.'
        }
        response_code = 201

    return response_object, response_code


def save_update(id, data: Dict[str, str]) -> None:
    website = db.session.query(Website).filter(Website.id == id)
    response_object = {
        'status': 'fail',
        'message': 'Website doesn\'t exist.'
    }
    response_code = 404
    if website:
        response_object = {
            'status': 'success',
            'message': 'Website successfully updated.'
        }
        response_code = 201
        website.update(data)
        # new_website = db.session.query(Website).filter(Website.id == id)
        # new_website.update(data)
        db.session.commit()

    return response_object, response_code


def get_all_websites():
    return Website.query.all()

def get_a_website(id):
    return Website.query.filter_by(id=id).first()

def save_changes(data: Website) -> None:
    db.session.add(data)
    db.session.commit()

def delete_a_website(data: Website) -> None:
    db.session.delete(data)
    db.session.commit()
