from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/')

from . import login
from . import register
from . import logout