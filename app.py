import requests
from random import randrange
from flask import Flask
from flask import jsonify, make_response
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


URL_POSTS = ' https://jsonplaceholder.typicode.com/posts'

mdb_client = MongoClient('mongodb://scsc:getdata@mongo:27017/')
db = mdb_client['sc']
col = db['posts']


@app.route('/')
def index():
    if not col.find_one():
        return 'No Data Available...Please use the /load endpoint'
    doc = col.find({}, {'_id': False}, skip=(randrange(50))).limit(1)[0]
    return make_response(jsonify(doc, 200))


@app.route('/load')
def load():
    data = requests.get(URL_POSTS).json()
    ids = col.insert_many(data).inserted_ids
    return make_response(jsonify(str(ids)), 201)


@app.route('/health')
def health():
    return make_response('OK', 200)


if __name__ == '__main__':
    app.run()
