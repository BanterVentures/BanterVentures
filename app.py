import os
import jinja2
import webapp2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({
            "startups": json.load(open('data/startups.json')),
            "investors": json.load(open('data/investors.json')),
            "mentors": json.load(open('data/mentors.json'))}))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=False)
