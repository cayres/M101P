"""Hello world with bottle and pymongo."""
import bottle
from pymongo import MongoClient


@bottle.route('/')
def index():
    """Return index page."""
    connection = MongoClient('localhost', 27017)

    db = connection.test

    name = db.names

    item = name.find_one()

    print '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)
