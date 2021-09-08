from .process import CarProcess
from serializers.serializers import CarSerializer


class CarHandler:
    def save_car(car: CarSerializer):
        return CarProcess.save_car(car)

    def get_car(query: dict = {}):
        return CarProcess.get_car(query)
