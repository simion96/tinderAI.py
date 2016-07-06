import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json
import urllib2
import requests

fbToken = os.getenv('FB_TOKEN')
fbID = os.getenv('FB_ID')


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


url = 'https://api.gotinder.com/auth'
headers ={'Content-Type': 'application/json', 'User-Agent':'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
payload = {'force_refresh' : 'False', 'facebook_id' : fbID, 'facebook_token' : fbToken}
r = requests.post(url, headers=headers, data = json.dumps(payload))


print 'token is: ' + str(fbToken)
print 'fbid is: ' + str(fbID)

rjson =  json.loads(r.text)
print "token is: " + rjson['token']
tinder_token = rjson['token']

tinder_headers = {'X-Auth-Token': tinder_token,
                  'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                  }
print tinder_headers

#getting reccomandations
url2 = 'https://api.gotinder.com/user/recs'

tinder_headers2 = {'X-Auth-Token': tinder_token,
                  'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                   'locale': 'en-GB'
                  }
r = requests.post(url2, headers = tinder_headers2)
recs_json = r.text
with open('data.txt', 'w') as outfile:
    json.dump(r.text, outfile, sort_keys=True, indent=4)
print r.url
print r.headers
print r.request
print r.status_code
print r.text




