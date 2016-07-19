import pprint
import sys
import os
import json
import time
import urllib2
from pprint import pprint
import requests
import datetime

fbToken = os.getenv('FB_TOKEN')
fbID = os.getenv('FB_ID')

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def write_file(file, data):
    with open(file, 'w') as outfile:
        outfile.write(data)

def read_file(file):
    with open(file, 'r') as outfile:
        return outfile.read()

def initialize():
    url = 'https://api.gotinder.com/auth'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
    payload = {'force_refresh': 'False', 'facebook_id': fbID, 'facebook_token': fbToken}
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    #print r.text
    rjson = json.loads(r.text)
    print "token is: " + rjson['token']
    return rjson['token']

tinder_token = initialize()


#print 'token is: ' + str(fbToken)
#print 'fbid is: ' + str(fbID)



tinder_headers = {'X-Auth-Token': tinder_token,
                  'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                  }
print tinder_headers

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
    recs_json2 = byteify(recs_json)
    print r.url
    print r.headers
    print r.request
    print r.status_code
    dict = json.loads(recs_json2)
    return dict['results']

#print type(dict)
print "------------LADIES--------------"

def like_recs():
    counter = 0
    try:
        while counter < 20:
            results = get_recs()
            liked = read_file("liked")
            instagrams = read_file("instagrams")
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
            write_file("liked", liked)
            write_file("instagrams", instagrams)
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
    print json.dumps(json.loads(r3.text), indent=4)
    return r3.text

while True:
    like_recs()

#print type(recs_json2)
#pprint(recs_json2)



like_headers2 = {'X-Auth-Token': tinder_token,
                   'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                   'firstPhotoID': 'en-GB'
                   }





