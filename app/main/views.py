from flask import render_template,request,redirect,url_for
from . import main 
from ..requests import  get_sources,get_articles

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    newsSource = get_sources()
    title = 'News Sources-catchup on whats latest'
    print(newsSource)
    return render_template('index.html',title = title, sources = newsSource)
@main.route('/article/<string:id>')
def source(id):
    '''
    View source page function that shows its source and details
    '''
    articles = get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
    