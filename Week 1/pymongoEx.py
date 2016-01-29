"""Testando Pymongo."""

from pymongo import MongoClient

# Connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

names = db.names

item = names.find_one()

print(item['name'])
