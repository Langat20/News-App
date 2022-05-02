from flask import Blueprint

#blueprint instance
main = Blueprint('main',__name__)
from . import views,error