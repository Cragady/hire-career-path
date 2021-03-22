import datetime

from app.main import db
from app.main.model.network import Network
from typing import Dict, Tuple
import json

def save_new_network(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    network = Network.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'fail',
        'message': 'Network already exists.'
    }
    response_code = 409

    if not network:
        new_network = Network(
            acquaintance=data['acquaintance'],
            company=data['company'],
            comms=data['comms'],
            comments=data['comments']
        )
        save_changes(new_network)
        response_object = {
            'status': 'success',
            'message': 'Network successfully saved.'
        }
        response_code = 201

    return response_object, response_code


def save_update(id, data: Dict[str, str]) -> None:
    network = db.session.query(Network).filter(Network.id == id)
    response_object = {
        'status': 'fail',
        'message': 'Network doesn\'t exist.'
    }
    response_code = 404
    if network:
        response_object = {
            'status': 'success',
            'message': 'Network successfully updated.'
        }
        response_code = 201
        network.update(data)
        # new_network = db.session.query(Network).filter(Network.id == id)
        # new_network.update(data)
        db.session.commit()

    return response_object, response_code


def get_all_networks():
    return Network.query.all()

def get_a_network(id):
    return Network.query.filter_by(id=id).first()

def save_changes(data: Network) -> None:
    db.session.add(data)
    db.session.commit()

def delete_a_network(data: Network) -> None:
    db.session.delete(data)
    db.session.commit()
