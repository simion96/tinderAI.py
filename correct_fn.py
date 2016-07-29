import glob

import os
import json
import time
import utils as utils
import requests
import datetime


config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]     
print "fbtoken is " + str(fbToken) 


source = glob.glob("2ndacc/to_correct/*")
ids = []
profiles = []
print source
for i in source:
    ids.append(i[19:43])
    print i[19:43]

profiles = []
with open('liked', 'r') as input:
    for line in input:
        for id in ids:
            if id in line:
                profiles.append(str(id) + " "  + str(utils.get_url(line)))
                #print "found one - " + str(id) + " url is " + str(utils.get_url(line))
        #print lines[9:33]
#print profiles


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

for profile in profiles:
    try:
        current = profile.split(' ')
        #current0 = id, current1 = link to first pic
        link = 'https://api.gotinder.com/like/{0}'.format(current[0])
        liking_header = {'X-Auth-Token': tinder_token,
                            'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                            'firstPhotoID': ''+str(current[1])
                            }
        likereq = requests.get(link, headers = liking_header)
        print 'status: ' + str(likereq.status_code) + ' text: ' + str(likereq.text)
        print str(current[0]) + " "  + str(current[1])
    except Exception as ex:
        print "hit an exception i guess"
        print ex