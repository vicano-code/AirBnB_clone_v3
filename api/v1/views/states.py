#!/usr/bin/python3
"""
Handles RESTFul API actions for state view
"""
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """retrieves the list of all state objects"""
    state_list = [obj.to_dict() for obj in storage.all('State').values()]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    """retrieves a state objects give its id"""
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    return jsonify(state_obj.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """delete as state object"""
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    storage.delete(state_obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """creates/post a state object to storage"""
    if not request.get_json():
        return jsonify({"error": "NOT a JSON"}), 400
    elif "name" not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    else:
        data_obj = request.get_json()
        obj = State(**data_obj)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """updates a state object"""
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    data_obj = request.get_json()
    if not data_obj:
        return jsonify({"error": "NOT a JSON"}), 400
    for k, v in data_obj.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(state_obj, k, v)
    state_obj.save()
    return jsonify(state_obj.to_dict()), 200
