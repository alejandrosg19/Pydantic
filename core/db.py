"""
Database Config
"""
from pymongo import MongoClient

database = MongoClient().WorkShopPydantic
car_collection = database.car_collection
