import datetime

from app.main import db
from app.main.model.interview import Interview
from typing import Dict, Tuple

def save_new_interview(data: Dict[str, str,]) -> Tuple[Dict[str, str], int]:
    interview = Interview.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'fail',
        'message': 'Interview already exists'
    }
    response_code = 409

    if not interview:
        new_interview = Interview(
            date=data['date'],
            interviewer=data['interviewer'],
            phone=data['phone'],
            comms=data['comms'],
            interview_address=data['interview_address'],
            mailing_address=data['mailing_address'],
            follow_up_date=data['follow_up_date'],
            comments=data['comments']
        )
        save_changes(new_interview)
        response_object = {
            'status': 'success',
            'message': 'Interview successfully saved.'
        }
        response_code = 201

    return response_object, response_code


def save_update(id, data: Dict[str, str]) -> None:
    interview = db.session.query(Interview).filter(Interview.id == id)
    response_object = {
        'status': 'fail',
        'message': 'Interview doesn\'t exist.'
    }
    response_code = 404
    if interview:
        response_object = {
            'status': 'success',
            'message': 'Interview successfully updated.'
        }
        response_code = 201
        interview.update(data)
        # new_interview = db.session.query(Interview).filter(Interview.id == id)
        # new_interview.update(data)
        db.session.commit()

    return response_object, response_code

def get_all_interviews():
    return Interview.query.all()

def get_an_interview(id):
    return Interview.query.filter_by(id=id).first()

def save_changes(data: Interview) -> None:
    db.session.add(data)
    db.session.commit()

def delete_an_interview(data: Interview) -> None:
    db.session.delete(data)
    db.session.commit()