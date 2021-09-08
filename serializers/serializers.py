from enum import Enum
from typing import Any, List, Dict, Optional, Type
from pydantic import BaseModel, Field, validator
from .docs_fields import description_of_chasis
from pydantic.color import Color


class ColorEnum(str, Enum):
    yellow = "yellow"
    blue = "blue"
    red = "red"


class MetaSerializer(BaseModel):
    message: str


class AdditionalSerializer(BaseModel):
    name: str
    others: Optional[dict]


class TuningSerializer(BaseModel):
    location: str
    costo: float
    color: Optional[Color]
    additional: Optional[AdditionalSerializer]

    @validator('color')
    def specific_name(cls, v):
        return v.original()


class WheelsSerializers(BaseModel):
    size: int
    mark: str
    rubber_gauge: Optional[str]

    class Config:
        @staticmethod
        def schema_extra(
                schema: Dict[str, Any],
                model: Type['WheelsSerializers']) -> None:
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)


class CarSerializer(BaseModel):
    """
    Data serializer class to build the car
    """
    # Validaciones especificas de campo
    model: int = Field(description="car model year", ge=2010, le=2021)

    # anotaciones de tipos
    # listas dinamicas
    wheels: List[Any] = Field(
        default=WheelsSerializers.schema(),
        description="accepts strings or WheelsSerializers instances"
    )

    # Field customization
    # descripción detallada .rst
    chassis: str = Field(
        title='Car chassis',
        description=description_of_chasis
    )

    # Enumeradores
    color: Optional[ColorEnum]

    # diccionario dinamico
    # profundamente aninada
    tuning: Optional[Dict[str, TuningSerializer]]

    # Validadores de campo especificos
    @validator('chassis')
    def specific_name(cls, v):
        list_cha = v.split('_')
        if len(list_cha) != 3:
            raise ValueError('does not follow the indicated parameters')
        return v

    @validator('wheels')
    def instance_wheels(cls, v):
        for item in v:
            if isinstance(item, str):
                break
            elif isinstance(item, dict):
                WheelsSerializers(**item)
                break
            else:
                raise ValueError('not is instance of Str or WheelsSerializers')
        return v

    class Config:
        schema_extra = {
            "example": {
                "model": 2015,
                "wheels": [
                    {"size": 12, "mark": "Michelin"},
                    "normal",
                ],
                "chassis": "ASDF_13L_2008",
                "color": "red",
                "tuning": {
                    "ailerons": {
                        "location": "back",
                        "costo": 1000,
                        "color": "purple",
                    },
                    "painting": {
                        "location": "all car",
                        "costo": 123.45,
                        "color": "black",
                    }
                }
            }
        }


class ResponseSerializer(BaseModel):
    status: bool = Field(
        description="True if the expected response is False otherwise"
    )
    message: str
    data: Any


class CarResponse(ResponseSerializer):
    data: List[CarSerializer] = Field(
        description="returns a list of cart objects"
    )


class CarResponseObj(ResponseSerializer):
    data: CarSerializer = Field(
        description="returns a car object"
    )


class QuerySerializer(BaseModel):
    id: Optional[str] = None
    color: Optional[ColorEnum] = None
