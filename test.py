import utils
import requests
import json

config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]     
print "fbtoken is " + str(fbToken) 

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

link = 'https://api.gotinder.com/like/{0}'.format("55b3e8a03163fe484fedbe22")
liking_header = {'X-Auth-Token': tinder_token,
                    'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                    'firstPhotoID': ''+str("{}").format("20aab89a-541f-4b14-8fbf-5757fccd8279")
                    }
likereq = requests.get(link, headers = liking_header)
print 'status: ' + str(likereq.status_code) + ' text: ' + str(likereq.text)
