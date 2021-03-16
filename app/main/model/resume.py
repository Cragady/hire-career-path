from .. import db
from typing import Union
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Resume(db.Model):
    """ Resume Model for storing resume submissions """
    __tablename__ = "resume_submissions"

    id = db.Column('resume_submission_id', db.Integer, primary_key=True, autoincrement=True)
    job = db.Column('job_applied_to', TINYTEXT)
    company = db.Column('company_name', TINYTEXT)
    contact = db.Column('contact_name_and_title', TINYTEXT)
    phone = db.Column(TINYTEXT)
    comms = db.Column('email_and_other_contact', TINYTEXT)
    address = db.Column('mailing_address', TINYTEXT)
    website = db.Column(TINYTEXT)
    date_submitted = db.Column('date_resume_submitted', DATETIME)
    cover_letter_date = db.Column('date_cover_letter_submitted', DATETIME)
    references = db.Column('references_sent', TEXT)
    discovered_by = db.Column('method_of_discovery', TEXT)
    job_description = db.Column('job_description_and_keywords', TEXT)
    status = db.Column('status_of_application', TEXT)
    comments = db.Column(TEXT)
    created_at = db.Column(DATETIME)
    updated_at = db.Column(DATETIME)