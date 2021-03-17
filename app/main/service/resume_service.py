import datetime

from app.main import db
from app.main.model.resume import Resume
from typing import Dict, Tuple

def save_new_resume(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    resume = Resume.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'fail',
        'message': 'Resume already exists.'
    }
    response_code = 409

    if not resume:
        new_resume = Resume(
            job=data['job'],
            company=data['company'],
            contact=data['contact'],
            phone=data['phone'],
            comms=data['comms'],
            address=data['address'],
            website=data['website'],
            date_submitted=data['date_submitted'],
            cover_letter_date=data['cover_letter_date'],
            references=data['references'],
            discovered_by=data['discovered_by'],
            job_description=data['job_description'],
            status=data['status'],
            comments=data['comments']
        )
        save_changes(new_resume)
        response_object = {
            'status': 'success',
            'message': 'Resume successfully saved.'
        }
        response_code = 201

    return response_object, response_code




def get_all_resumes():
    return Resume.query.all()

def get_a_resume(id):
    return Resume.query.filter_by(id=id).first()

def save_changes(data: Resume) -> None:
    db.session.add(data)
    db.session.commit()

def delete_a_resume(data: Resume) -> None:
    db.session.delete(data)
    db.session.commit()