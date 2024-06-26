#!/usr/bin/python3
"""
    app for registering blueprint and starting flask
"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(self):
    """close storage query after each session"""
    storage.close()


@app.errorhandler(404)
def handle_404_error(e):
    """returns a JSON-formatted 404 status code response"""
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response


@app.route('/api/v1/nop')
def api_v1_nop():
    """returns the 404 error via this route"""
    return handle_404_error(None)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", '0.0.0.0'),
            port=int(getenv("HBNB_API_PORT", '5000')), threaded=True)
