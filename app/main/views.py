from flask import render_template
from . import main 
from ..request import  get_sources,get_articles

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')