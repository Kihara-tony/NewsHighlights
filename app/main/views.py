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
@main.route('/article/<string:id>')
def source(id):
    '''
    View source page function that shows its source and details
    '''
    articles = get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
    