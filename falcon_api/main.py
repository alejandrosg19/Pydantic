import falcon
from falcon_api.app.api.urls import routers
from falcon_api.app.api.v1.views import api

app = falcon.API()

# load views
for (path, resource) in routers:
    app.add_route(path, resource)

api.register(app)
