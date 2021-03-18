from .. import db
from sqlalchemy.dialects.mysql import TEXT, TINYTEXT, DATETIME

class Network(db.Model):
    """ Network Model for storing contacts for network opportunities """
    __tablename__ = "networking_acquaintances"

    id = db.Column('network_id', db.Integer, primary_key=True, autoincrement=True)
    acquaintance = db.Column('acquaintance_name_and_title', TINYTEXT)
    company = db.Column('company_name', TINYTEXT)
    comms = db.Column('contact_information', TINYTEXT)
    comments = db.Column(TEXT)
    created_at = db.Column(DATETIME)
    updated_at = db.Column(DATETIME)