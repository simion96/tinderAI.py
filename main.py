import pprint
import sys
import os
import json
import time
import urllib2
from pprint import pprint
import requests
import datetime
import numpy as np
from skimage.feature import hog
from scipy.misc import imread,imresize,imsave
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import glob
import pickle
import urllib
from PIL import Image
from AI.predictor import Predictor
import scipy.misc
import warnings
import utils as utils
warnings.filterwarnings(action="ignore", category=DeprecationWarning)


config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]     

def initialize():
    url = 'https://api.gotinder.com/auth'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
    payload = {'force_refresh': 'False', 'facebook_id': fbID, 'facebook_token': fbToken}
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    rjson = json.loads(r.text)
    return rjson['token']

tinder_token = initialize()
tinder_headers = {'X-Auth-Token': tinder_token,
                  'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                  }

#getting reccomandations
def get_recs():
    url2 = 'https://api.gotinder.com/user/recs'

    tinder_headers2 = {'X-Auth-Token': tinder_token,
                      'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                       'locale': 'en-GB'
                      }
    r = requests.post(url2, headers = tinder_headers2)
    with open('data.txt', 'w') as outfile:
        json.dump(r.text, outfile, sort_keys=True, indent=4)
    with open('data.txt') as data_file:
        recs_json = json.load(data_file)
    recs_json2 = utils.byteify(recs_json)
    dict = json.loads(recs_json2)
    return dict['results']

#print type(dict)
print "------------LADIES--------------"

def like_recs():
    counter = 0
    try:
        while counter < 20:
            results = get_recs()
            liked = utils.read_file("liked")
            instagrams = utils.read_file("/Instagram/instagrams")
            for i in results:
                time.sleep(1)
                link = 'https://api.gotinder.com/like/{0}'.format(i["_id"])
                liking_header = {'X-Auth-Token': tinder_token,
                                 'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                                 'firstPhotoID': ''+str(i['photos'][0]['id'])
                                 }
                likereq = requests.get(link, headers = liking_header)
                print i['name'] + ' - ' +  i['_id']
                print 'status: ' + str(likereq.status_code) + ' text: ' + str(likereq.text)
                liked += str(i['name']) + ' - ' + str(i['_id']) + ' - ' + str(i['photos'][0]['url']) + '\n'
                try:
                    if 'instagram' in i:
                      instagrams+= str(i['instagram']['username'] + " ")
                    else:
                        print "no instagram mate soz"
                except KeyError as ex:
                    print 'nah mate'
                #print "photoid " + str(i['photos'][0]['id'])
            utils.write_file("liked", liked)
            utils.write_file("/Instagram/instagrams", instagrams)
            counter += 1

    except Exception as ex:
        print "hit an exception i guess"
        print ex

#err this actually gets matches, but could still be useful at some point
def get_updates():
    timenow = datetime.datetime.now().isoformat()
    print timenow
    tinder_headers3 = {'X-Auth-Token': tinder_token,
                       'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                       'last_activity_date': '{}'.format(timenow)
                       }
    url3 = 'https://api.gotinder.com/updates'
    r3 = requests.post(url3, headers = tinder_headers3)
    return r3.text

def like_recs_AI():
    try:
        folder = "ladiesAI/"
        extension = ".jpg"
        counter = 0
        while True:
            results = get_recs()
            liked = utils.read_file("liked")
            instagrams = utils.read_file("/Instagram/instagrams")
            for i in results:
                time.sleep(1)
                like = 'https://api.gotinder.com/like/{0}'.format(i["_id"])
                dislike = 'https://api.gotinder.com/pass/{0}'.format(i["_id"])
                liking_header = {'X-Auth-Token': tinder_token,
                                 'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                                 'firstPhotoID': '' + str(i['photos'][0]['id'])
                                 }
                #img - tinder img url, path = path on physical device, urllib saves the picture
                img = str(i['photos'][0]['url'])
                path = folder+img[27:51]+extension
                urllib.urlretrieve(str(i['photos'][0]['url']), path)
                result = Predictor.predict(path)
                if result == "G":
                    req = requests.get(like, headers = liking_header)
                elif result == "B":
                    req = requests.get(dislike, headers = liking_header)
                    liked += str(i['name']) + ' - ' + str(i['_id']) + ' - ' + str(i['photos'][0]['url']) + '\n'
                try:
                    if 'instagram' in i:
                        instagrams += str(i['instagram']['username'] + " ")
                    else:
                        print "no instagram mate soz"
                except KeyError as ex:
                    print 'nah mate'

            utils.write_file("liked", liked)
            utils.write_file("/Instagram/instagrams", instagrams)
            counter += 1

    except Exception as ex:
        print "hit an exception i guess"
        print ex

while True:
    like_recs_AI()

like_headers2 = {'X-Auth-Token': tinder_token,
                   'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                   'firstPhotoID': 'en-GB'
                   }





