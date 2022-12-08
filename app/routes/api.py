# Below contains APi endpoints
from flask import Blueprint
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')
