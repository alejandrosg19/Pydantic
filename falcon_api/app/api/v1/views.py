import falcon
from spectree import Response
from spectree import SpecTree
from serializers.serializers import (
    MetaSerializer,
    CarSerializer,
    CarResponseObj,
    QuerySerializer
)
from core.handler import CarHandler
from core.utils import make_query

api = SpecTree(
    "falcon",
    title="Falcon Docs",
    path="docs"
)


class RootViews:
    @api.validate(
        resp=Response(
            HTTP_200=MetaSerializer,
        ), tags=['Meta']
    )
    def on_get(self, request, response, **kwargs):
        """
        Root of host
        """
        output = {
            'message': 'Falcon API'
        }
        response.status = falcon.HTTP_200
        response.media = output


class HealthView:
    @api.validate(
        resp=Response(
            HTTP_200=MetaSerializer,
        ),
        tags=['Meta']
    )
    def on_get(self, request, response, **kwargs):
        """
        Check health of service
        """
        output = {
            "message": "Status OK",
        }
        response.status = falcon.HTTP_200
        response.media = output


class APIViews:
    @api.validate(
        json=CarSerializer,
        resp=Response(
            HTTP_200=CarResponseObj,
        ),
        tags=['API']
    )
    def on_post(self, request, response, **kwargs):
        """
        Save new car
        """
        car = request.context.json
        output = CarHandler.save_car(car)
        response.status = falcon.HTTP_200
        response.media = output


class APIViewsGet:
    @api.validate(
        query=QuerySerializer,
        resp=Response(
            HTTP_200=None,
        ),
        tags=['API']
    )
    def on_get(self, request, response, **kwargs):
        """
        Save new car
        """
        query = make_query(**request.params)
        output = CarHandler.get_car(query)
        response.status = falcon.HTTP_200
        response.media = output
