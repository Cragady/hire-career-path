from flask import request
from flask_restx import Resource

from ..util.dto import WebsiteDto
from app.main.service.website_service import save_new_website, get_all_websites, get_a_website, delete_a_website, save_update
from typing import Dict, Tuple

api = WebsiteDto.api
_website = WebsiteDto.website

@api.route('/')
class WebsiteList(Resource):
    @api.doc('list_of_websites')
    @api.marshal_list_with(_website, envelope='data')
    def get(self):
        return get_all_websites()

    @api.expect(_website, validate=True)
    @api.response(201, 'Website successfully created.')
    @api.doc('create a new website')
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_new_website(data=data)


@api.route('/<id>')
@api.param('id', 'The Website identifier')
@api.response(404, 'Website not found.')
class Website(Resource):
    @api.doc('get a website')
    @api.marshal_with(_website)
    def get(self, id):
        website = get_a_website(id)
        if not website:
            api.abort(404, 'Website not found.')
        else:
            return website

    @api.doc('delete a website')
    def delete(self, id):
        website = get_a_website(id)
        if not website:
            api.abort(404, 'Website not found.')
        else:
            delete_a_website(website)
            return ({
                'status': 'success',
                'message': 'Successfully deleted website.'
            }, 200)

    @api.expect(_website, validate=True)
    @api.response(201, 'Website successfully updated.')
    @api.doc('update a website')
    def post(self, id) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_update(id, data=data)