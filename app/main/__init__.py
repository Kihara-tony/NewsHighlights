from flask import Blueprint
#initializing app
app = Blueprint('main',__name__)
from . import views,error