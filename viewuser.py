import requests
import utils as utils
import json
import urllib2
import urllib
import os

config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]
base_url = "https://api.gotinder.com/"
recs_endpoint = "user/recs"
loc_endpoint = "user/ping"
friends_endpoint = "group/friends"

def initialize():
    url = 'https://api.gotinder.com/auth'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
    payload = {'force_refresh': 'False', 'facebook_id': fbID, 'facebook_token': fbToken}
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    rjson = json.loads(r.text)
    return rjson['token']

tinder_token = initialize()

def test():
    headers = {'Content-Type': 'application/json',
                'User-agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)',
                'app-version': '3',
                'platform' : 'ios',
                'X-Auth-Token': tinder_token,
                'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                }
    r = requests.get(base_url+friends_endpoint, headers = headers)
    return json.loads(r.text)

def getUserData(user):
    tinder_headers3 = {'X-Auth-Token': tinder_token,
                       'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                       }
    url3 = 'https://api.gotinder.com/user/{0}'.format(user)
    r3 = requests.get(url3, headers = tinder_headers3)
    return json.loads(r3.text)

def getFriendIDs():
    ids = []
    results = test()
    userids = results["results"]
    for u in userids:
        ids.append(u["user_id"])
    return ids

def auto_stalk():
    folder = "fbUsers/"
    sep = "/"
    extension = ".jpg"
    counter = 0
    userImgCount = 0
    smallist = []
    smallist.append(getFriendIDs()[1])
    for friend in getFriendIDs():
        jsonUserData = getUserData(friend)
        name = jsonUserData['results']['name']
        images = []
        userImgCount = 0
        folderName = folder+name+str(counter)
        for i in jsonUserData['results']['photos']:
            image = i["url"]
            if not os.path.exists(folderName):
                os.makedirs(folderName)
            path = folder+name+str(counter)+sep+str(userImgCount)+extension
            urllib.urlretrieve(str(image), path)
            userImgCount += 1
        utils.write_file(folderName+sep+"bio.txt", jsonUserData['results']['bio'].encode('utf-8'))
        counter += 1

        
auto_stalk()

