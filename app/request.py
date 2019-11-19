from app import app
import urllib.request
import json
from .models import news

Sources = news.Sources
Articles = news.Articles


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news sources base url
base_url = app.config['SOURCES_API_BASE_URL']

# Getting the articles base url
articles_url = app.config['ARTICLES_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_results_list):
    '''
    Function that processes the sources result and transform them to a list of Objects
    Args:
        news_list: a list of dictionaries that contain news sources details
    '''

    sources_results = []
    for sources_item in sources_results_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        author = sources_item.get('author')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        if language == 'en' and country == 'us':
            sources_object = Sources(
                id, name, author, description, url, category, language, country)
            sources_results.append(sources_object)
    print('*********************************************')
    print(sources_results)
    return sources_results


# Articles

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_url.format(id)

    with urllib.request.urlopen(get_articles_url+api_key) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        print(get_articles_response)
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_result(articles_results_list)

    return articles_results


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

        articles_object = Articles(
            id, name, author, description, url, image, publishedAt, content)
        articles_results.append(articles_object)

    return articles_results
