from .. import db
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Website(db.Model):
    """ Website Model for storing info on a career search website """
    __tablename__ = "career_websites"

    id = db.Column('career_website_id', db.Integer, primary_key=True, autoincrement=True)
    website = db.Column(TINYTEXT)
    username = db.Column(TINYTEXT)
    resume_date = db.Column('date_resume_posted', DATETIME)
    cover_letter_date = db.Column('date_cover_letter_posted', DATETIME)
    comments = db.Column(TEXT)
    created_at = db.Column(DATETIME)
    updated_at = db.Column(DATETIME)