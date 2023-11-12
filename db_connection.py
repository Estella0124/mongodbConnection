import pymongo

url = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(url)
# this is an ex
db = client['folkmusicdb']

