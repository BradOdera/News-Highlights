
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..news import Sources

# views
@main.route('/')
def index():
    '''
    root page that returns the index page
    '''

    # Getting news sources
    sources = get_sources('general')
    print('******************general_news************')
    print(sources)
    
    #getting sources
    return render_template('trial.html', sources = sources)


@main.route('/articles/<id>')
def articles(id):

    articles = get_articles(id)
    print('***********articlesbyID*************')
    print(articles)

    return render_template('articles.html',articles = articles)