from flask_testing import TestCase
import os

from app.main import db
from manage import app


class BaseTestCase(TestCase):
    """ Basic Setup """

    def create_app(self):
        app.config.from_object(os.environ['APP_SETTINGS'])
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()