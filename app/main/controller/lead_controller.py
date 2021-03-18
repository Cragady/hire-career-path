from flask import request
from flask_restx import Resource

from ..util.dto import LeadDto
from app.main.service.lead_service import save_new_lead, get_all_leads, get_a_lead, delete_a_lead, save_update
from typing import Dict, Tuple

api = LeadDto.api
_lead = LeadDto.lead

@api.route('/')
class LeadList(Resource):
    @api.doc('list_of_leads')
    @api.marshal_list_with(_lead, envelope='data')
    def get(self):
        return get_all_leads()

    @api.expect(_lead, validate=True)
    @api.response(201, 'Lead successfully created.')
    @api.doc('create a new lead')
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_new_lead(data=data)


@api.route('/<id>')
@api.param('id', 'The Lead identifier')
@api.response(404, 'Lead not found.')
class Lead(Resource):
    @api.doc('get a lead')
    @api.marshal_with(_lead)
    def get(self, id):
        lead = get_a_lead(id)
        if not lead:
            api.abort(404, 'Lead not found.')
        else:
            return lead

    @api.doc('delete a lead')
    def delete(self, id):
        lead = get_a_lead(id)
        if not lead:
            api.abort(404, 'Lead not found.')
        else:
            delete_a_lead(lead)
            return ({
                'status': 'success',
                'message': 'Successfully deleted lead.'
            }, 200)

    @api.expect(_lead, validate=True)
    @api.response(201, 'Lead successfully updated.')
    @api.doc('update a lead')
    def post(self, id) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_update(id, data=data)