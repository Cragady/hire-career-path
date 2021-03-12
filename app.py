import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Config - Change this setup for production
DEBUG = True

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r'/*': {'origins': '*'}})

# test route
@app.route('/api/test/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
