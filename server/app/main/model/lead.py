from .. import db
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Lead(db.Model):
    """ Lead Model for storing leads given by those in your network """
    __tablename__ = "leads"

    id = db.Column('lead_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('lead_name_and_title', TINYTEXT)
    company = db.Column(TINYTEXT)
    comms = db.Column('contact_information', TINYTEXT)
    comments = db.Column(TEXT)
    created_at = db.Column(TINYTEXT)
    updated_at = db.Column(TINYTEXT)