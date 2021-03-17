from .. import db
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Networking(db.Model):
    """ Networking Model for storing contacts for networking opportunities """
    __tablename__ = "networking"

    id = db.Column('networking_id', db.Integer, primary_key=True, autoincrement=True)
    acquaintance = db.Column('acquaintance_name_and_title', TINYTEXT)
    company = db.Column('company_name', TINYTEXT)
    comms = db.Column('contact_information', TINYTEXT)
    comments = db.Column(TEXT)
    created_at = db.Column(DATETIME)
    updated_at = db.Column(DATETIME)