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




url = 'https://api.gotinder.com/auth'
headers ={'Content-Type': 'application/json', 'User-Agent':'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
payload = {'force_refresh' : 'False', 'facebook_id' : fbID, 'facebook_token' : fbToken}
r = requests.post(url, headers=headers, data = json.dumps(payload))
print headers
print r.url
print r.headers
print r.request
print r.status_code

print 'token is: ' + str(fbToken)
print 'fbid is: ' + str(fbID)
print json.dumps(r.text, indent=4, sort_keys=True)


