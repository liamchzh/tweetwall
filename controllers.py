# coding: utf-8

import tornado.web
import settings
from twitter import *
import json

class Base(tornado.web.RequestHandler):
    def search(self, q):
        t = Twitter(auth=OAuth(settings.OAUTH_TOKEN, settings.OAUTH_SECRET,
                       settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
           )
        # Search the latest tweets
        return t.search.tweets(q=str(q))


class Index(Base):
    def get(self):
        topic = self.get_arguments("topic")
        if topic:
            data = self.search(topic[0])
            self.render("index.html", tweets=data['statuses'])
        else:
            self.render("index.html", tweets=None)


class Search(Base):
    def get(self, q):
        self.write(self.search(q))
