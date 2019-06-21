from flask import Blueprint
#initializing app
app = Blueprint('main',__name__)
from app import views,error