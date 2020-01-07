# from app import create_app
# from flask_script import Manager, Server
#  # from flask.ext.script import Manager
#
# # Creating app instance
# app = create_app('development')
# manager = Manager(app)
# manager.add_command('server', Server)
#
#
# @manager.command
# def test():
#     """
#     Run the unit tests.
#     """
#     import unittest
#
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
#
#
# if __name__ == '__main__':
#     manager.run()

from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route("/")
def home():
    newsapi = NewsApiClient(api_key="fc44e252019a4642b8194a9006c9a279")
    topstories = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topstories['articles']

    img = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])

    mylist = zip(img, desc)

    return render_template('landing.html', context=mylist)


@app.route('/index')
def index():
    newsapi = NewsApiClient(api_key="fc44e252019a4642b8194a9006c9a279")
    topstories = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topstories['articles']

    desc = []
    news = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)

    return render_template('index.html', context=mylist)


@app.route('/BBC')
def BBC():
    newsapi = NewsApiClient(api_key="fc44e252019a4642b8194a9006c9a279")
    topstories = newsapi.get_top_headlines(sources="bbc-news")

    articles = topstories['articles']
    desc = []
    news = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)

    return render_template('BBC.html', context=mylist)



@app.route('/Axios')
def Axios():
    newsapi = NewsApiClient(api_key="fc44e252019a4642b8194a9006c9a279")
    topstories = newsapi.get_top_headlines(sources="axios")

    articles = topstories['articles']
    desc = []
    news = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)

    return render_template('Axios.html', context=mylist)




if __name__ == "__main__":
    app.run(debug=True)
