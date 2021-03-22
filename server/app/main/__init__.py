import os
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    cors.init_app(app, resources={r'/*': {'origins': '*'}})
    db.init_app(app)

    # test route
    @app.route('/api/test/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    return app