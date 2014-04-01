'''
Created on Mar 24, 2014

@author: sgopinath
'''
from flask.ext.restful import Resource, Api
from flask import Markup
import decorators
import pymongo
from bson.json_util import dumps

from urlparse import urljoin
from flask import request
from atom import AtomFeed


client = pymongo.MongoClient(host='mongodb://mongo01.dev.nymag.biz:27017', w=1, j=True)

class PartnerFeeds(Resource):
    '''
    classdocs
    '''
    
    def make_external(self, url):
        return urljoin(request.url_root, url)

    
    @decorators.jsonp
    def get(self, api_key=None):
        db = client.articles
        
        feed = AtomFeed(title='Articles Feed', link_self='somelink', feed_id='someid', author='NY Media', entries=None)
        articles = db.articles.find().limit(15)
        for article in articles:
            feed.add(article['entryTitle'], unicode(article['excerpt']),
                     content_type='html',
                     author=article.get('authoredBy', ''),
                     url=article['canonicalUrl'],
                     updated=article.get('publishDate', ''),
                     published=article.get('publishDate', ''))

        return  dumps(feed.to_string())
    
    