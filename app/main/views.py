from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_topstories, get_categories, get_newsupdates


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news and categorically arranged news
    top_stories = get_topstories('google-news')
    print(top_stories)
    title = 'News highlights'
    tech = get_categories('technology')
    entertainment = get_categories('entertainment')
    business = get_categories('business')
    sports = get_categories('sports')

    return render_template('index.html', title=title, google_news=top_stories, biz=business, tech=tech,
                           ent=entertainment, sprt=sports)

    # @main.route('/update/<id>')
    # def article(id):
    #     detz_articles = get_newsupdates(id)
    #     print(detz_articles)
    #     return render_template('news.html', detz=detz_articles)
