#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images


administrator1 = users.User("wenwenzhang1001@gmail.com")
administrator2 = users.User("")

class Event(ndb.Model):
    name = ndb.StringProperty(required= True)
    description = ndb.StringProperty()
    coverurl=ndb.StringProperty()

    authorID = ndb.StringProperty(default="administrator")
    author_name = ndb.StringProperty(default="administrator")

    loc = ndb.GeoPtProperty(required=True,default=db.GeoPt(0,0))
    date = ndb.DateTimeProperty(required=True)

    linkage = ndb.StringProperty()


class Crowdworker(ndb.Model):
    ID = ndb.StringProperty()
    name = ndb.StringProperty()
    rated_times = ndb.IntegerProperty()
    score = ndb.IntegerProperty()




class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class ViewAllEvents(webapp2.RequestHandler):
    def get(self):


class ViewOneEvent(webapp2.RequestHandler):
    def get(self):

class GiveFeedback(webapp2.RequestHandler):
    def get(self):

class AddEvent(webapp2.RequestHandler):
    def get(self):

class DeleteEvent(webapp2.RequestHandler):
    def get(self):



class ViewAllWorkers(webapp2.RequestHandler):
    def get(self):

class ViewOneWorker(webapp2.RequestHandler):
    def get(self):



class MapView(webapp2.RequestHandler):
    def get(self):

class CalendarView(webapp2.RequestHandler):
    def get(self):





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Mapview',MapView),
    ('/Calendarview',CalendarView),
    ('/Addevent',AddEvent),
    ('/ViewOneEvent',ViewOneEvent),
    ('/ViewAllEvents',ViewAllEvents),
    ('/ViewOneWorker',ViewOneWorker),
    ('/ViewAllWorkers',ViewAllWorkers),
    ('/GiveFeedback',GiveFeedback),
    ('/DeleteEvent',DeleteEvent)
], debug=True)

