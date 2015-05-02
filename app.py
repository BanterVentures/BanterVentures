import os
import jinja2
import webapp2
from google.appengine.api import urlfetch
import json
import Queue

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        response = urlfetch.fetch("https://raw.githubusercontent.com/BanterVentures/Portfolio/master/startups.json")
        startups = json.loads(response.content)
        q = Queue.Queue()
        q.put("2ecc71", "3498db")
        while True:
            if len(startups) % 3 == 0:
                break
            else:
                startups.append({"image_650x350": "http://placehold.it/650x350/" + q.get() + "/000000&text=Coming soon..."})

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({"startups": startups}))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
