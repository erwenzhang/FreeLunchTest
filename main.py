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
# limitations under the License
from __future__ import division
import webapp2
import cgi
import urllib
import json

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images


administrator1 = users.User("wenwenzhang1001@gmail.com")
administrator2 = users.User("kevin@utexas.edu.com")
administrator1ID = administrator1.user_id()
administrator2ID = administrator2.user_id()

class Event(ndb.Model):
    name = ndb.StringProperty(required= True)
    description = ndb.StringProperty()
    coverurl=ndb.StringProperty(default=None)

    authorID = ndb.StringProperty(default="administrator")
    author_name = ndb.StringProperty(default="administrator")

    loc = ndb.GeoPtProperty(required=True,default=ndb.GeoPt(0,0))
    date = ndb.DateTimeProperty(required=True)

    linkage = ndb.StringProperty(default=None)


class Crowdworker(ndb.Model):
    ID = ndb.StringProperty()
    name = ndb.StringProperty()
    rated_times = ndb.IntegerProperty(default=0)
    score = ndb.IntegerProperty()




class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class ViewAllEvents(webapp2.RequestHandler):
    def get(self):
        events = Event.query().fetch()
        locations = []
        dates = []
        names = []

        for event in events:
            locations.append(event.loc)
            dates.append(event.date)
            names.append(event.name)

        dictPassed = {'dates':dates, 'names':names,'locations':locations}
        jsonObj = json.dumps(dictPassed, sort_keys=True,indent=4, separators=(',', ': '))
        self.response.write(jsonObj)



class ViewOneEvent(webapp2.RequestHandler):
    def get(self):
        event_name = self.request.get("event_name")
        the_event = ndb.gql("SELECT * FROM Event WHERE name = :1",event_name).get()
        print event_name
        author = ndb.gql("SELECT * FROM Crowdworker WHERE ID = :1",the_event.authorID).get()
        if author.ID != administrator1ID and author.ID != administrator2ID:
            ratings = str(author.score/author.rated_times)
            author_name = author.name
            print "ratings: "+ratings
        else:
            ratings = None
            author_name = None

        dictPassed = {'date':the_event.date,
                      'location':the_event.loc,
                      'description':the_event.description,
                      'coverUrl':the_event.coverUrl,
                      'linkage':the_event.linkage,
                      'ratings':ratings,
                      'author_name':author_name
                      }
        jsonObj = json.dumps(dictPassed, sort_keys=True,indent=4, separators=(',', ': '))
        self.response.write(jsonObj)


class GiveFeedback(webapp2.RequestHandler):
    def get(self):
        feedback = self.request.get('feedback')
        author_name = self.request.get('author_name')
        author = ndb.gql("SELECT * FROM Crowdworker WHERE name = :1",author_name).get()
        author.rated_times +=1
        if feedback == "Yes":
            author.score +=5

        author.put()




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/Mapview',MapView),
    # ('/Calendarview',CalendarView),
    # ('/Addevent',AddEvent),
    ('/ViewOneEvent',ViewOneEvent),
    ('/ViewAllEvents',ViewAllEvents),
    # ('/ViewOneWorker',ViewOneWorker),
    # ('/ViewAllWorkers',ViewAllWorkers),
    ('/GiveFeedback',GiveFeedback),
    # ('/DeleteEvent',DeleteEvent)
], debug=True)

