# -*- coding: utf-8 -*-


import json
import time
import pymongo
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
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
    for s in star.aggregate([{'$match': {'categorie': "middle-east"}}, {'$sample': {'size': 10}}]):
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
    for s in star.aggregate([{'$match': {'categorie': "world"}}, {'$sample': {'size': 10}}]):
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
    for s in star.aggregate([{'$match': {'categorie': "sport"}}, {'$sample': {'size': 10}}]):
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
    for s in star.aggregate([{'$match': {'categorie': "tech"}}, {'$sample': {'size': 10}}]):
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
    for s in star.aggregate([{'$match': {'categorie': "business"}}, {'$sample': {'size': 10}}]):
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
    output = [{'items': out}]
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

    # out = out.replace('\\', '')

    out = json.dumps(out, indent=4)
    out = json.loads(out)

    return out


@app.route('/getKeywords', methods=['GET'])
def getKeywords():
    collection = mongo.db.false_keywords
    out = []
    for s in collection.find().sort([("frequency", pymongo.DESCENDING)]):
        if len(s['keyword'])>1:
            out.append({'keyword': (s['keyword']),
                        'frequency': (s['frequency'])
                        })
    return jsonify(out)


@app.route('/searchKeywords', methods=['POST'])
def searchKeywords():
    articles = []
    if not request.json or not 'keywords' in request.json:
        abort(400)
    article = {
        'keywords': request.json['keywords']
    }
    articles.append(article)
    article = json.dumps(article)
    data = json.loads(article)
    keyword = data['keywords']
    keyword = keyword.split(',')
    collection = mongo.db.articles
    output = []
    for s in collection.find({"keywords": {"$in": keyword}}):
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


@app.route('/getaltarticle', methods=['POST'])
def get_alt_article():
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


@app.route('/addrel', methods=['GET'])
def add_rel():
    star = mongo.db.articles
    star.update(
        {},
        {"$set": {"related_articles": []}},
        upsert=True, multi=True
    )
    output = []
    return jsonify(output)


# get related articles after getting id
@app.route('/getRel', methods=['POST'])
def insert_rel():
    star = mongo.db.articles
    # the keywords and ids
    key_id = []
    # test
    output = []
    # the output
    putout = []

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

    for s in star.find({'_id': ObjectId(id)}):
        key_id.append({'keywords': s['keywords'],
                       'url': s['url']})
    for key in key_id:
        keywords = key['keywords']
        # list of titles
        rel = []
        for s in star.find({"keywords": {"$in": keywords}}):
            url = s['url']
            title = s['title']
            pic = s['pic']

            orig_url = key['url']

            if url == orig_url:
                continue
            else:
                rel.append(url)
                putout.append({'orig_url': key['url'],
                               'related_url': url,
                               'related_title': title,
                               'related_pic': pic,
                               })

    return json.dumps({'result': putout}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/getCountries', methods=['GET'])
def get_countries():
    output = []
    star = mongo.db.countries
    star_star = mongo.db.false_keywords

    start_time = time.time()

    countries_codes = {}

    for s in star.find():
        country = (s['country'])

        countries_codes[country] = s['country_code']

    for key in countries_codes:
        for s in star_star.find({'keyword': key}):
            output.append({'code': countries_codes[key],
                           'frequency': s['frequency']})

    print ("My program took ", time.time()-start_time, " to run")
    #return json.dumps({'result': output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
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
