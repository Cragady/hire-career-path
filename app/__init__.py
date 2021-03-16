from flask_restx import Api
from flask import Blueprint

from .main.controller.resume_controller import api as resume_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title='JOB TRACKER',
    version='1.0',
    description='A rest api that will work as a backend for a job tracking web app.'
    )

api.add_namespace(resume_ns, path='/resume')