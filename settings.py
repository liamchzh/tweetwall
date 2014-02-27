# coding: utf-8

import os
import controllers 

settings = {"template_path" : os.path.join(os.path.dirname(__file__), "templates")}

urls = [(r'/tweetwall', controllers.Index),
        (r'/search/(\w+)', controllers.Search),
        ]


OAUTH_TOKEN = '581110929-7DouolaD8KrBhCydPsJj7PE2QLgaOZm7PTbagDKI'
OAUTH_SECRET = '2KJYy1Wr59tzpHDlr8PEgBl3ndv7BBl4kqPjwfGLxkVlq'
CONSUMER_KEY = 'zm6diL9l948WDWT7m7Efw'
CONSUMER_SECRET = 'bnm8cOkJfGcMQPTkow6iYlZLvrQAVykkLduj0RgH3Q'
