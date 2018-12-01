#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
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
    for s in collection.find().limit(20).sort([("frequency", pymongo.DESCENDING)]):
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
    collection = mongo.db.false_articles
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

    star = mongo.db.false_articles
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
    star = mongo.db.false_articles
    star.update(
        {},
        {"$set": {"related_articles": []}},
        upsert=True, multi=True
    )
    output = []
    return jsonify(output)


@app.route('/insertrel', methods=['GET'])
def insert_rel():
    star = mongo.db.false_articles
    # the keywords and ids
    key_id = []
    # test
    output = []
    # the output
    putout = []
    for s in star.find():
        key_id.append({'keywords': s['keywords'],
                       'id': str(s['_id']),
                       'title': s['title'],
                       'url': s['url']})
    for key in key_id:
        keywords = key['keywords']
        # list of titles
        tits = []
        for s in star.find({"keywords": {"$in": keywords}}):
            url = s['url']
            orig_url = key['url']
            if url == orig_url:
                continue
            else:
                tits.append(url)
        putout.append({'orig_url': key['url'],
                       'related_urls': tits})

    return json.dumps({'result': putout}, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


@app.route('/getCountries', methods=['GET'])
def get_countries():
    output = []
    countries = {'إيران': 'IR', 'الولايات المتحدة': 'US', 'جزر جوادلوب': 'GP', 'آيسلندا': 'IS', 'أثيوبيا': 'ET', 'أذربيجان': 'AZ',
                 'أراض فرنسية جنوبية': 'TF', 'أرمينيا': 'AM', 'أروبا': 'AW', 'أستراليا': 'AU', 'ألبانيا': 'AL',
                 'ألمانيا': 'DE', 'أنتاركتيكا': 'AQ', 'أنتيغوا/بربودا': 'AG', 'أنجويلا': 'AI', 'أندورا': 'AD',
                 'أندونيسيا': 'ID', 'أنغولا': 'AO', 'أورغواي': 'UY', 'أوزباكستان': 'UZ', 'أوغندا': 'UG',
                 'أوكرانيا': 'UA', 'أيرلندا': 'IE', 'إريتريا': 'ER', 'إسبانيا': 'ES', 'إكوادور': 'EC',
                 'إلسلفادور': 'SV', 'إيطاليا': 'IT', 'استونيا': 'EE', 'الأرجنتين': 'AR', 'الأردن': 'JO',
                 'الإمارات العربية المتحدة': 'AE', 'الباهاماس': 'BS', 'البحرين': 'BH', 'أفغانستان': 'AF',
                 'البرازيل': 'BR', 'البرتغال': 'PT', 'البوسنة/الهرسك': 'BA', 'الجبل الأسو': 'ME', 'الجزائر': 'DZ',
                 'الجزر العذراء الأمريكي': 'VI', 'الجزر العذراء البريطانية': 'VG', 'الجمهورية التشيكية': 'CZ',
                 'الجمهورية الدومينيكية': 'DO', 'الدانمارك': 'DK', 'الرأس الأخضر': 'CV', 'السنغال': 'SN',
                 'السودان': 'SD', 'السويد': 'SE', 'الصحراء الغربية': 'EH', 'الصومال': 'SO', 'الصين': 'CN',
                 'العراق': 'IQ', 'الغابون': 'GA', 'الفليبين': 'PH', 'الكونغو': 'CG', 'الكويت': 'KW', 'المالديف': 'MV',
                 'المغرب': 'MA', 'المكسيك': 'MX', 'المملكة العربية السعودية': 'SA', 'المملكة المتحدة': 'GB',
                 'النرويج': 'NO', 'النمسا': 'AT', 'النيجر': 'NE', 'الهند': 'IN', 'اليابان': 'JP', 'اليمن': 'YE',
                 'اليونان': 'GR', 'بابوا غينيا الجديدة': 'PG', 'باراغواي': 'PY', 'باكستان': 'PK', 'بالاو': 'PW',
                 'بربادوس': 'BB', 'بروني': 'BN', 'بلجيكا': 'BE', 'بلغاريا': 'BG', 'بنغلاديش': 'BD', 'بنما': 'PA',
                 'بنين': 'BJ', 'بوتان': 'BT', 'بوتسوانا': 'BW', 'بورتوريكو': 'PR', 'بوركينا فاسو': 'BF',
                 'بوروندي': 'BI', 'بولندا': 'PL', 'بوليفيا': 'BO', 'بولينيزيا الفرنسية': 'PF', 'بيتكيرن': 'PN',
                 'بيرو': 'PE', 'بيليز': 'BZ', 'تايلندا': 'TH', 'تايوان': 'TW', 'تركمانستان': 'TM', 'تركيا': 'TR',
                 'ترينيداد وتوباغو': 'TT', 'تشاد': 'TD', 'تنزانيا': 'TZ', 'توغو': 'TG', 'توفالو': 'TV', 'توكلو': 'TK',
                 'تونس': 'TN', 'تونغا': 'TO', 'تيمور الشرقية': 'TL', 'جبل طارق': 'GI', 'جرينلاند': 'GL',
                 'جزر أولند': 'AX', 'جزر الأنتيل الهولندي': 'AN', 'جزر القمر': 'KM',
                 'جزر الولايات المتحدة الصغيرة': 'UM', 'جزر برمود': 'BM', 'جزر توركس/كايكوس': 'TC', 'جزر سليمان': 'SB',
                 'جزر فارو': 'FO', 'جزر فوكلاند(المالديف)': 'FK', 'جزر كايمان': 'KY', 'جزر كوك': 'CK',
                 'جزر كوكس(كيلينغ)': 'CC', 'جزر مارشال': 'MH', 'جزر ماريانا الشمالية': 'MP', 'جزيرة بوفيه': 'BV',
                 'جزيرة كريسماس': 'CX', 'جزيرة مان': 'IM', 'جزيرة نورفولك': 'NF', 'جزيرة هيرد/جزر ماكدونالد': 'HM',
                 'جمايكا': 'JM', 'جمهورية أفريقيا الوسطى': 'CF', 'جنوب أفريقيا': 'ZA', 'جوام': 'GU',
                 'جورجيا الجنوبية/جزر ساندويتش': 'GS', 'جيبوتي': 'DJ', 'جيرزي': 'JE', 'جيورجيا': 'GE',
                 'دولة مدينة الفاتيكان': 'VA', 'دومينيكا': 'DM', 'رواندا': 'RW', 'روسيا': 'RU', 'روسيا البيضاء': 'BY',
                 'رومانيا': 'RO', 'ريونيون': 'RE', 'زامبيا': 'ZM', 'زمبابوي': 'ZW', 'ساحل العاج': 'CI', 'ساموا': 'WS',
                 'ساموا الأمريكية': 'AS', 'سان مارينو': 'SM', 'سانت بارتليمي': 'BL', 'سانت بيير/ميكلون': 'PM',
                 'سانت فنسنت/الجرينادين': 'VC', 'سانت كيتس/نيفيس': 'KN', 'سانت لوسيا': 'LC', 'سانت مارتن': 'MF',
                 'سانت هيلانة': 'SH', 'سريلانكا': 'LK', 'سلوفاكيا': 'SK', 'سلوفينيا': 'SI', 'سنغافورة': 'SG',
                 'سوازيلند': 'SZ', 'سورية': 'SY', 'سورينام': 'SR', 'سويسرا': 'CH', 'سيراليون': 'SL', 'سيشيل': 'SC',
                 'شيلي': 'CL', 'صربيا': 'RS', 'طاجيكستان': 'TJ', 'عُمان': 'OM', 'غامبيا': 'GM', 'غانا': 'GH',
                 'غرينادا': 'GD', 'غواتيمال': 'GT', 'غويانا الفرنسية': 'GF', 'غيانا': 'GY', 'غيرنزي': 'GG',
                 'غينيا': 'GN', 'غينيا الاستوائي': 'GQ', 'غينيا-بيساو': 'GW', 'فانواتو': 'VU', 'فرنسا': 'FR',
                 'فلسطين': 'PS', 'فنزويلا': 'VE', 'فنلندا': 'FI', 'فيتنام': 'VN', 'فيجي': 'FJ', 'قبرص': 'CY',
                 'قطر': 'QA', 'قيرغيزستان': 'KG', 'كازاخستان': 'KZ', 'كاليدونيا الجديدة': 'NC', 'كاميرون': 'CM',
                 'كرواتيا': 'HR', 'كمبوديا': 'KH', 'كندا': 'CA', 'كوبا': 'CU', 'كوريا الجنوبية': 'KR',
                 'كوريا الشمالية': 'KP', 'كوستاريكا': 'CR', 'كولومبيا': 'CO', 'كيريباتي': 'KI', 'كينيا': 'KE',
                 'لاتفيا': 'LV', 'لاوس': 'LA', 'لبنان': 'LB', 'لتوانيا': 'LT', 'لوكسمبورغ': 'LU', 'ليبيا': 'LY',
                 'ليبيريا': 'LR', 'ليختنشتين': 'LI', 'ليسوتو': 'LS', 'مارتينيك': 'MQ', 'ماكاو': 'MO', 'مالاوي': 'MW',
                 'مالطا': 'MT', 'مالي': 'ML', 'ماليزيا': 'MY', 'مايوت': 'YT', 'مدغشقر': 'MG', 'مصر': 'EG',
                 'مقدونيا': 'MK', 'منغوليا': 'MN', 'موريتانيا': 'MR', 'موريشيوس': 'MU', 'موزمبيق': 'MZ',
                 'مولدافيا': 'MD', 'موناكو': 'MC', 'مونتسيرات': 'MS', 'ميانمار': 'MM', 'ميكرونيسيا': 'FM',
                 'ناميبيا': 'NA', 'ناورو': 'NR', 'نيبال': 'NP', 'نيجيريا': 'NG', 'نيكاراجوا': 'NI', 'نيوزيلندا': 'NZ',
                 'نييوي': 'NU', 'هايتي': 'HT', 'هندوراس': 'HN', 'هنغاريا': 'HU', 'هولندا': 'NL', 'هونغ كونغ': 'HK'}
    star = mongo.db.false_keywords
    for s in star.find():
        word = s['keyword']
        freq = s['frequency']

        if word in countries:
            output.append({'word': word,
                           'cunt': next(iter(countries))})
        else:
            output.append({'word': word,
                           'mal': next(iter(countries))})
            # output.append({#'country': countries[word],
            #                'frequency': freq})
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
