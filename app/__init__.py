from flask_restx import Api
from flask import Blueprint

from .main.controller.resume_controller import api as resume_ns
from .main.controller.interview_controller import api as interview_ns
from .main.controller.network_controller import api as network_ns
from .main.controller.lead_controller import api as lead_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title='JOB TRACKER',
    version='1.0',
    description='A rest api that will work as a backend for a job tracking web app.'
    )

api.add_namespace(resume_ns, path='/resume')
api.add_namespace(interview_ns, path='/interview')
api.add_namespace(network_ns, path='/network')
api.add_namespace(lead_ns, path='/lead')