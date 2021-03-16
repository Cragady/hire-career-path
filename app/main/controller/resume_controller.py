from flask import request
from flask_restx import Resource

from ..util.dto import ResumeDto
from app.main.service.resume_service import save_new_resume, get_all_resumes, get_a_resume, delete_a_resume
from typing import Dict, Tuple

api = ResumeDto.api
_resume = ResumeDto.resume

@api.route('/')
class ResumeList(Resource):
    @api.doc('list_of_resumes')
    @api.marshal_list_with(_resume, envelope='data')
    def get(self):
        return get_all_resumes()

    @api.expect(_resume, validate=True)
    @api.response(201, 'Resume successfully created.')
    @api.doc('create a new resume')
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return save_new_resume(data=data)


@api.route('/<id>')
@api.param('id', 'The Resume identifier')
@api.response(404, 'Resume not found.')
class Resume(Resource):
    @api.doc('get a resume')
    @api.marshal_with(_resume)
    def get(self, id):
        resume = get_a_resume(id)
        if not resume:
            api.abort(404)
        else:
            return resume

    @api.doc('delete a resume')
    def delete(self, id):
        resume = get_a_resume(id)
        if not resume:
            api.abort(404)
        else:
            delete_a_resume(resume)