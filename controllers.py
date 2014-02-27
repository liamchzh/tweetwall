# coding: utf-8

import tornado.web
import settings
from twitter import *

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class Search(tornado.web.RequestHandler):
    def get(self, q):
        self.write(self.search(q))

    def search(self, q):
        t = Twitter(
            auth=OAuth(settings.OAUTH_TOKEN, settings.OAUTH_SECRET,
                       settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
           )

        # Search the latest tweets
        return t.search.tweets(q='#'+str(q))
