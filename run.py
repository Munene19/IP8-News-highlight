from Flask import flask
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="65034e770a4f45ffaeafc84d023e3ca4")
    Headlines = newsapi.get_top_headlines(sources=bbc - news)


    articles = topheadlines['articles']
