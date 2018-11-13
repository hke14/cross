# mongo.py

import json
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

app = Flask(__name__)

CORS(app)

app.config['MONGO_DBNAME'] = 'newsaggregartor'
app.config['MONGO_URI'] = 'mongodb://gnr011:Kalash1@ds040309.mlab.com:40309/newsaggregartor'

mongo = PyMongo(app)


@app.route("/")
@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.articles
    output = []
    for s in star.find():
        output.append({'title': s['title'],
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
        output.append({'title': s['title'],
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
        output.append({'title': s['title'],
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
        output.append({'title': s['title'],
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
        output.append({'title': s['title'],
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
        output.append({'title': s['title'],
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
    for s in star.aggregate([{'$sample': {'size': 5}}]):
        output.append({'title': s['title'],
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
    # return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/getopposing', methods=['GET'])

@app.route('/bull')
def add():
    user = mongo.db.users
    user.insert_one({'name': 'Anthony'})
    return 'Added user'


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
