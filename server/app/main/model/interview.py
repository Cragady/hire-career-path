from .. import db
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Interview(db.Model):
    """ Interview Model for storing interviews """
    __tablename__ = "interviews"

    id = db.Column('interview_id', db.Integer, primary_key=True, autoincrement=True)
    date = db.Column('interview_date', DATETIME)
    interviewer = db.Column('interviewer_name_and_title', TINYTEXT)
    phone = db.Column(TINYTEXT)
    comms = db.Column('email_and_other_contact', TINYTEXT)
    interview_address = db.Column(TINYTEXT)
    mailing_address = db.Column(TINYTEXT)
    follow_up_date = db.Column(DATETIME)
    comments = db.Column(TEXT)
    created_at = db.Column(DATETIME)
    updated_at = db.Column(DATETIME)
