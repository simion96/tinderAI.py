import requests
import utils as utils
import json

config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]
id = "577c21342e59a643122ad465"
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

def get_updates():
    tinder_headers3 = {'X-Auth-Token': tinder_token,
                       'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                       }
    url3 = 'https://api.gotinder.com/user/{0}'.format(id)
    r3 = requests.get(url3, headers = tinder_headers3)
    print json.dumps(json.loads(r3.text), indent=4)
    return r3.text

get_updates()