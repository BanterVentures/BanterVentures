import os
import jinja2
import webapp2
from google.appengine.api import urlfetch
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        startups = json.loads(urlfetch.fetch("https://raw.githubusercontent.com/BanterVentures/Portfolio/master/startups.json").content)
        investors = json.loads(urlfetch.fetch("https://raw.githubusercontent.com/BanterVentures/Portfolio/master/data/investors.json").content)
        mentors = json.loads(urlfetch.fetch("https://raw.githubusercontent.com/BanterVentures/Portfolio/master/data/mentors.json").content)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({"startups": startups, "investors": investors, "mentors": mentors}))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
