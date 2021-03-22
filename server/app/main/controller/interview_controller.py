from flask import request
from flask_restx import Resource

from ..util.dto import InterviewDto
from app.main.service.interview_service import save_new_interview, get_all_interviews, get_an_interview, delete_an_interview, save_update
from typing import Dict, Tuple

api = InterviewDto.api
_interview = InterviewDto.interview

@api.route('/')
class InterviewList(Resource):
    @api.doc('list of interviews')
    @api.marshal_list_with(_interview, envelope='data')
    def get(self):
        return get_all_interviews()

    @api.expect(_interview, validate=True)
    @api.response(201, 'Interview successfully created.')
    @api.doc('create a new interview')
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_new_interview(data=data)


@api.route('/<id>')
@api.param('id', 'The Interview identifier')
@api.response(404, 'Interview not found.')
class Interview(Resource):
    @api.doc('get an interview')
    @api.marshal_with(_interview)
    def get(self, id):
        interview = get_an_interview(id)
        if not interview:
            api.abort(404, 'Interview not found.')
        else:
            return interview

    @api.doc('delete an interview')
    def delete(self, id):
        interview = get_an_interview(id)
        if not interview:
            api.abort(404, 'Interview not found.')
        else:
            delete_an_interview(interview)
            return ({
                'status': 'success',
                'message': 'Successfully deleted interview.'
            })

    @api.expect(_interview, validate=True)
    @api.response(201, 'Interview successfully updated.')
    @api.doc('update an interview')
    def post(self, id) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_update(id, data=data)



# @api.route('/<link_id>')
# @api.param('link_id', 'The foreign key.')
# @api.response(404, 'No interviews found on this company')
# class LinkedInterview(Resource):
#     @api.doc('get the related interviews')
#     @api.marshal_with(_interview)
#     def get(self, link_id):
#         interviews = get_related_interviews(link_id)
#         if not interviews:
#             api.abort('No interviews found on this company')
#         else:
#             return interviews