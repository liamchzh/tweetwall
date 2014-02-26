# coding: utf-8

import tornado.web
from settings import *
from twitter import *

class Index(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World.")

class Search(tornado.web.RequestHandler):
    def get(self, q):
        print search(q)

    def search(q):
        t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

        # Search the latest tweets
        return t.search.tweets(q)
