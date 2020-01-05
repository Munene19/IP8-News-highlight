import os


class Config:
    '''
    General configuration parent class
    '''

    TOPSTORIES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=fc44e252019a4642b8194a9006c9a279'
    CATEGORIES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=fc44e252019a4642b8194a9006c9a279'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fc44e252019a4642b8194a9006c9a279'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
