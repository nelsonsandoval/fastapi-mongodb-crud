#import statements
from pymongo import MongoClient

#create DB connection
connection = MongoClient("mongodb://localhost:27017/test")