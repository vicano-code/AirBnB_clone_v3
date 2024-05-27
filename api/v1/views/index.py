#!/usr/bin/python3
"""
    flask with general routes
    routes:
        /status:    display "status":"OK"
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models import classes


@app_views.route('/status')
def status():
    """return JSON status of OK"""
    return jsonify({'status': 'OK'})

@app_views.route('/api/v1/stats')
def storage_counts():
    """retrieves the number of objects in each class"""
    cls_counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }}
    return jsonify(cls_counts)
