import os
import re
import json

import webapp2
import jinja2

from google.appengine.ext import ndb

from google.appengine.api import mail

from helpers import prefix_routes

prefix = "tutor"

template_dir = os.path.join(os.path.dirname(__file__), prefix, 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=False)

class Message(ndb.Model):
    content = ndb.JsonProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

def quoted(s):
    l = re.findall('\'([^\']*)\'', str(s))
    if l:
        return l[0]
    return None

jinja_env.filters['quoted'] = quoted

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render(self, template, **kw):
        self.response.out.write(render_str(template,**kw))

class MainHandler(Handler):
    def get(self):
        self.render('index.html')

routes = [
    ('/', MainHandler),
]

routes = prefix_routes(routes,'/tutor')
app = webapp2.WSGIApplication(routes, debug=True)
