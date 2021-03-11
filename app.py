from flask import Flask, jsonify
from flask_cors import CORS

# Config - Change this setup for production
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# test route
@app.route('/api/test/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
