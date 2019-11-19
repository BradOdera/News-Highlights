from flask import render_template
from app import app
from .request import get_sources,get_articles

# views
@app.route('/')
def index():
    '''
    root page that returns the index page
    '''

    # Getting news sources
    sources = get_sources()
    
    #getting articles 
    # articles = get_articles()


    return render_template('index.html', source = sources)


@app.route('/sources/<id>')
def sources(id):
    '''
    news page function that returns news details page
    '''
    sources = get_sources()
    heading = None
    for source in sources:
        if id == source.id:
            heading = source.name

    articles = get_articles(id)

    return render_template('articles.html',article = articles , heading  = heading)