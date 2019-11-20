
import urllib.request
import json
from .news import Sources,Articles

api_key = None
# Getting the movie base url
base_url = None

articles_url=None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category,api_key)
    print('*****get_sources_url**********')
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function that processes the sources result and transform them to a list of Objects
    Args:
        news_list: a list of dictionaries that contain news sources details
    '''

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        author = sources_item.get('author')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        
        sources_object = Sources(id, name, author, description, url, category, language, country)
        sources_results.append(sources_object)
    
    return sources_results


# Articles

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_url.format(id,api_key)
    print('are you fetching anything')
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_result = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_result = process_result(articles_results_list)

    return articles_result


def process_result(articles_list):
    '''
    Function that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: a list of dictionaries that contain news articles details
    '''

    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        author = articles_item.get('author')
        description = articles_item.get('description')
        url = articles_item.get('url')
        image = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        articles_object = Articles(id, name, author, description, url, image, publishedAt, content)
        articles_results.append(articles_object)

    return articles_results
