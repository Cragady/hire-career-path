import datetime

from app.main import db
from app.main.model.lead import Lead
from typing import Dict, Tuple
import json

def save_new_lead(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    lead = Lead.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'fail',
        'message': 'Lead already exists.'
    }
    response_code = 409

    if not lead:
        new_lead = Lead(
            name=data['name'],
            company=data['company'],
            comms=data['comms'],
            comments=data['comments']
        )
        save_changes(new_lead)
        response_object = {
            'status': 'success',
            'message': 'Lead successfully saved.'
        }
        response_code = 201

    return response_object, response_code


def save_update(id, data: Dict[str, str]) -> None:
    lead = db.session.query(Lead).filter(Lead.id == id)
    response_object = {
        'status': 'fail',
        'message': 'Lead doesn\'t exist.'
    }
    response_code = 404
    if lead:
        response_object = {
            'status': 'success',
            'message': 'Lead successfully updated.'
        }
        response_code = 201
        lead.update(data)
        # new_lead = db.session.query(Lead).filter(Lead.id == id)
        # new_lead.update(data)
        db.session.commit()

    return response_object, response_code


def get_all_leads():
    return Lead.query.all()

def get_a_lead(id):
    return Lead.query.filter_by(id=id).first()

def save_changes(data: Lead) -> None:
    db.session.add(data)
    db.session.commit()

def delete_a_lead(data: Lead) -> None:
    db.session.delete(data)
    db.session.commit()
