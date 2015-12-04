#!/usr/bin/env python

import webapp2
import cgi
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images

administrator1 = users.User("wenwenzhang1001@gmail.com")
# administrator2 = users.User("")

class Event(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    coverurl = ndb.StringProperty()
    authorID = ndb.StringProperty(default="administrator")
    author_name = ndb.StringProperty(default="administrator")
    loc = ndb.GeoPtProperty(required=True,default=ndb.GeoPt(0,0))
    date = ndb.DateTimeProperty(required=True)
    linkage = ndb.StringProperty()

class Crowdworker(ndb.Model):
    ID = ndb.StringProperty()
    name = ndb.StringProperty()
    rated_times = ndb.IntegerProperty()
    score = ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class AddEvent(webapp2.RequestHandler):
    def

app = webapp2.WSGIApplication([
    ('/', MainHandler)#,
    # ('/Mapview',MapView),
    # ('/Calendarview',CalendarView),
    # ('/Addevent',AddEvent),
    # ('/ViewOneEvent',ViewOneEvent),
    # ('/ViewAllEvents',ViewAllEvents),
    # ('/ViewOneWorker',ViewOneWorker),
    # ('/ViewAllWorkers',ViewAllWorkers),
    # ('/GiveFeedback',GiveFeedback),
    # ('/DeleteEvent',DeleteEvent)
], debug=True)

