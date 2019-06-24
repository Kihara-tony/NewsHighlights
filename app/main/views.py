from flask import render_template
from . import main 
from ..request import  get_sources,get_articles

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    newsSource= get_sources()
    title = 'News Sources-catchup on whats latest'
    print(newsSource)
    return render_template('index.html',title=title, sources=newsSource)
@main.route('/articles/<string:id>')
def source(id):
    '''
    View source page function that shows its source and details
    '''
    articles = get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
    