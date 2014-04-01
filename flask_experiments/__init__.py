from flask import Flask
from flask.ext import restful

# api endpoints
from todo import todo_simple
from partner_feeds import views

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(views.PartnerFeeds, '/partner/feeds/<string:api_key>')
