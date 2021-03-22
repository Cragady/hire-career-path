from flask import request
from flask_restx import Resource

from ..util.dto import NetworkDto
from app.main.service.network_service import save_new_network, get_all_networks, get_a_network, delete_a_network, save_update
from typing import Dict, Tuple

api = NetworkDto.api
_network = NetworkDto.network

@api.route('/')
class NetworkList(Resource):
    @api.doc('list_of_networks')
    @api.marshal_list_with(_network, envelope='data')
    def get(self):
        return get_all_networks()

    @api.expect(_network, validate=True)
    @api.response(201, 'Network successfully created.')
    @api.doc('create a new network')
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_new_network(data=data)


@api.route('/<id>')
@api.param('id', 'The Network identifier')
@api.response(404, 'Network not found.')
class Network(Resource):
    @api.doc('get a network')
    @api.marshal_with(_network)
    def get(self, id):
        network = get_a_network(id)
        if not network:
            api.abort(404, 'Network not found.')
        else:
            return network

    @api.doc('delete a network')
    def delete(self, id):
        network = get_a_network(id)
        if not network:
            api.abort(404, 'Network not found.')
        else:
            delete_a_network(network)
            return ({
                'status': 'success',
                'message': 'Successfully deleted network.'
            }, 200)

    @api.expect(_network, validate=True)
    @api.response(201, 'Network successfully updated.')
    @api.doc('update a network')
    def post(self, id) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_update(id, data=data)