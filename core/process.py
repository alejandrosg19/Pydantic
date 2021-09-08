from .db import car_collection
from serializers.serializers import CarSerializer


class CarProcess:
    def save_car(car: CarSerializer):
        car_dict = car.dict()
        car_collection.insert_one(car_dict)
        car_dict['_id'] = str(car_dict['_id'])
        return car_dict

    def get_car(query: dict):
        response = car_collection.find(query)
        car_list = []
        for car_dict in response:
            car_dict['_id'] = str(car_dict['_id'])
            car_list.append(car_dict)
        return car_list
