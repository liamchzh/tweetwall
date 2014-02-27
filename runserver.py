# coding: utf-8

import tornado.ioloop
import settings

application = tornado.web.Application(settings.urls, **settings.settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
