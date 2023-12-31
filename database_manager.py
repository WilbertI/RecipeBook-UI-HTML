from pymongo import MongoClient
from bson import ObjectId
import yaml

with open('config.cfg', 'r') as file:
    config = yaml.safe_load(file)

connection = config['mongo']['address'].format(user = config['mongo']['user'], password = config['mongo']['password'])
database = MongoClient(connection)['RecipeBook']


def insert(table, record):
    collection = database[table]
    record_id = collection.insert_one(record).inserted_id
    return str(record_id)

def find(table, id):
    collection = database[table]
    record = collection.find_one({'_id': ObjectId(id)})
    record['_id'] = str(record['_id'])
    return record

def gather(table):
    collection = database[table]
    records = list(collection.find())
    return records
