# mongo.py

from flask import Flask, make_response
from flask import jsonify
from flask import request
import json
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'george'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/george'

mongo = PyMongo(app)



@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.articles
  output = []
  for s in star.find():
    output.append({'title' : s['title'], 'date': s['date_str'], 'art_content': s['art_content']})
  return json.dumps({'result' : output}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/bull')
def add():
    user = mongo.db.users
    user.insert_one({'name' : 'Anthony'})
    return 'Added user'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/star/', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})
