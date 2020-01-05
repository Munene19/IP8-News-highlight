import urllib.request, json
from .models import Topstories, Categories, NewsUpdate

# Getting api key
api_key = None

# Getting the news api base urls
base_url = None
base2_url = None
base3_url = None


def configure_request(app):
    global api_key, base_url, base2_url, base3_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["TOPSTORIES_API_BASE_URL"]
    base2_url = app.config["CATEGORIES_API_BASE_URL"]
    base3_url = app.config["ARTICLES_BASE_URL"]


def get_topstories(source):
    """
    Function that gets the json response to our url request
    """
    get_topstories_url = base_url.format(source)

    with urllib.request.urlopen(get_topstories_url) as url:
        get_topstories_data = url.read()
        get_topstories_response = json.loads(get_topstories_data)
        print(get_topstories_response)
        topstories_results = None

        if get_topnews_response['articles']:
            topnews_results_list = get_topnews_response['articles']
            topnews_results = process_results(topnews_results_list)

    return topnews_results


def process_results(topnews_list):
    '''
    Function  that processes the topnews result and transform them to a list of objects
    Args:
        topnews_list: A list of dictionaries that contain topnews details
    Returns :
        topnews_results: A list of topnews objects
    '''
    topnews_results = []
    for topnews_item in topnews_list:
        name = topnews_item.get('name')
        title = topnews_item.get('title')
        author = topnews_item.get('author')
        description = topnews_item.get('description')
        urlToImage = topnews_item.get('urlToImage')
        url = topnews_item.get('url')

        if urlToImage:
            topnews_object = TopNews(name, author, title, description, urlToImage, url)
            topnews_results.append(topnews_object)

    return topnews_results


def get_categories(category):
    """
    Function that gets the json response to our url request
    """
    get_categories_url = base2_url.format(category)

    with urllib.request.urlopen(get_categories_url) as url:
        get_categories_data = url.read()
        get_categories_response = json.loads(get_categories_data)
        print(get_categories_response)
        categories_results = None

        if get_categories_response['sources']:
            categories_results_list = get_categories_response['sources']
            categories_results = process2_results(categories_results_list)

    return categories_results


def process2_results(categories_list):
    '''
    Function  that processes the categories result and transform them to a list of objects
    Args:
        categories_lis A list of dictionaries that contain categories details
t:
    Returns :
        caegoriess_results: A list of categories objects
    '''
    categories_results = []
    for categories_item in categories_list:
        id = categories_item.get('id')
        name = categories_item.get('name')
        description = categories_item.get('description')
        url = categories_item.get('url')

        if id:
            categories_object = Categories(id, name, description, url)
            categories_results.append(categories_object)

    return categories_results


def get_newsupdates(id):
    """
    Function that gets the json response to our url request
    """
    get_newsupdates_url = base3_url.format(id)
    print(get_newsupdates_url)

    with urllib.request.urlopen(get_newsupdates_url) as url:
        get_newsupdates_data = url.read()
        get_newsupdates_response = json.loads(get_newsupdates_data)

        newsupdates_results = None

        if get_newsupdates_response['articles']:
            newsupdates_results_list = get_newsupdates_response['articles']
            newsupdates_results = process3_results(newsupdates_results_list)

    return newsupdates_results


def process3_results(newsupdates_list):
    '''
    Function  that processes the newsupdate result and transform them to a list of objects
    Args:
        newsupdates_list: A list of dictionaries that contain category news' details
    Returns :
        newsupdates_results: A list of newsupdate objects
    '''
    newsupdates_results = []
    for newsupdate_item in newsupdates_list:
        id = newsupdate_item.get('id')
        author = newsupdate_item.get('author')
        title = newsupdate_item.get('title')
        description = newsupdate_item.get('description')
        url = newsupdate_item.get('url')
        urlToImage = newsupdate_item.get('urlToImage')
        publishedAt = newsupdate_item.get('publishedAt')

        newsupdates_object = NewsUpdate(id, author, title, description, url, urlToImage, publishedAt)
        newsupdates_results.append(newsupdates_object)

    return newsupdates_results
