
from flask import Blueprint

lists = Blueprint("lists", __name__, url_prefix="/lists")

from . import views
