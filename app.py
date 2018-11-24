# mongo.py

import json
import pymongo

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from flask import abort
from bson.objectid import ObjectId
import re


app = Flask(__name__)

CORS(app)

app.config['MONGO_DBNAME'] = 'newsaggregartor'
app.config['MONGO_URI'] = 'mongodb://gnr011:Kalash1@ds040309.mlab.com:40309/newsaggregartor'
app.config['JSON_SORT_KEYS'] = False

mongo = PyMongo(app)


@app.route("/")
@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.articles
    output = []
    for s in star.find():
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/middle-east', methods=['GET'])
def get_all_middle_east():
    star = mongo.db.articles
    output = []
    for s in star.find({'categorie': 'middle-east'}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/world', methods=['GET'])
def get_all_world():
    star = mongo.db.articles
    output = []
    for s in star.find({'categorie': 'world'}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/sport', methods=['GET'])
def get_all_sport():
    star = mongo.db.articles
    output = []
    for s in star.find({'categorie': 'sport'}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/tech', methods=['GET'])
def get_all_tech():
    star = mongo.db.articles
    output = []
    for s in star.find({'categorie': 'tech'}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/business', methods=['GET'])
def get_all_business():
    star = mongo.db.articles
    output = []
    for s in star.find({'categorie': 'business'}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/random', methods=['GET'])
def get_five_random():
    star = mongo.db.articles
    output = []
    for s in star.aggregate([{'$sample': {'size': 10}}]):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/Keywords', methods=['GET'])
def get_opposing():
    star = mongo.db.articles
    art_title = request.args.get('title')
    output = []
    for s in star.find({'title': art_title}):
        output.append({'title': s['title'], 'keywords': s['keywords']})
    output_json = jsonify(output)
    return output_json


@app.route('/getarticle', methods=['POST'])
def get_article():
    articles = []
    if not request.json or not 'id' in request.json:
        abort(400)
    article = {
        'id': request.json['id']
    }
    articles.append(article)
    article = json.dumps(article)
    data = json.loads(article)
    id = data['id']

    star = mongo.db.articles
    output = []
    for s in star.find({'_id': ObjectId(id)}):
        output.append({'id': str(s['_id']),
                       'title': s['title'],
                       'date': s['date_str'],
                       'art_content': s['art_content'],
                       'url': s['url'],
                       'pic': s['pic'],
                       'tag': s['tag'],
                       'tagu': s['tagu'],
                       'keywords': s['keywords'],
                       'score': s['score']})
    return jsonify(output)


@app.route('/bull')
def add():
    user = mongo.db.users
    user.insert_one({'name': 'Anthony'})
    return 'Added user'


@app.route('/gimme', methods=['GET'])
def get_all():
    collection = mongo.db.articles
    out = []
    for s in collection.find():
        out.append({'id': str(s['_id']),
                    'title': s['title'],
                    'date': s['date_str'],
                    'art_content': s['art_content'],
                    'url': s['url'],
                    'pic': s['pic'],
                    'tag': s['tag'],
                    'tagu': s['tagu'],
                    'keywords': s['keywords'],
                    'score': s['score']})
    return jsonify(output)


@app.route('/trial', methods=['GET'])
def trial():
    collection = """
{  
   "results":[  
      {  
         "title":"Result Title",
         "url":"/optional/url/on/click",
         "image":"optional-image.jpg",
         "price":"Optional Price",
         "description":"Optional Description"
      },
      {  
         "title":"Result Title",
         "description":"Result Description"
      }
   ]
}
    """
    collection = json.dumps(collection, indent=4, sort_keys=True)
    collection = json.loads(collection)

    return collection


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    collection = mongo.db.articles
    out = []
    rgx = re.compile('.*' + query + '.*', re.IGNORECASE)

    for s in collection.find({"title": rgx}):
        out.append({"title": s['title'],
                    "id": str(s['_id']),
                    "image": s['pic']
                    })
    out = str(json.dumps(out))

    out = """{"results":""" + out + "}"

    #out = out.replace('\\', '')

    out = json.dumps(out, indent=4)
    out = json.loads(out)

    return out

@app.route('/getKeywords', methods=['GET'])
def getKeywords():
    collection = mongo.db.false_keywords
    out = []
    for s in collection.find().limit(20).sort([("frequency", pymongo.DESCENDING)]):
        out.append({'keyword': (s['keyword']),
                    'frequency': (s['frequency'])
                    })
    output = [{'items': out}]
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result': output})
