from flask import Blueprint
from api.v1.views.index import *
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
