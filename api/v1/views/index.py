#!/usr/bin/python3
"""
    flask with general routes
    routes:
        /status:    display "status":"OK"
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """return JSON status of OK"""
    return jsonify({'status': 'OK'})
