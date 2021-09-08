from typing import Optional
from fastapi import APIRouter

from serializers.serializers import CarSerializer
from serializers.serializers import ColorEnum
from serializers.serializers import CarResponse, CarResponseObj
from serializers.serializers import MetaSerializer
from core.handler import CarHandler
from core.utils import make_query

router = APIRouter()


@router.post("/car/create", tags=["API"], response_model=CarResponseObj)
def create_car(car: CarSerializer):
    output = CarHandler.save_car(car)
    return {
        "status": True,
        "message": "Parked car",
        "data": output,
    }


@router.get(
    "/car/consult",
    tags=["API"],
    responses={
        200: {"model": CarResponse},
        400: {"model": MetaSerializer, "description": "Very Bad Request"}
    })
def get_car(
        id: Optional[str] = None,
        color: Optional[ColorEnum] = None):
    query = make_query(id, color)
    output = CarHandler.get_car(query)
    return {
        "status": True,
        "message": "Data of car",
        "data": output,
    }
