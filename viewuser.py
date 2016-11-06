import requests
import utils as utils
import json
import urllib2
import urllib
import os

config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]
#id = "577c21342e59a643122ad465"
#id = "5727a450cf8096b21fa31d7d" #Tashan Jehuty Rayleonard
#id = "55bfdcea909b20b824165988" #"Tony Fishman Lagarde
#id = "529db81422665fc16800001e" #Samuel Evans
#id = "540f69ba6cd05aff3543cbc8" #Joe Bell
#id = "5286a1e99f843c7f61000016" #Anthony Stec
#id = "575c82cd7553e1b41bb67465" #Alexander Miles
#id = "53e6207582d63f2e07c17da0" #Messy Uzunov
#id = "5296e1efca7ddbc760000054" #lucy willibean mair
#id = "52def403176f1d435c00024e" #Nikhil Thapar
#id = "5724db6c3380cdcd0b51fb6c" #George Miller
#id = "572931dc48c488f413c77e69" #Alex Forbes-Reed
#id = "5775d26658593a0056e354fd" #Vandan Thakkar
#id = "5371c4c113be222e160058af" #Chloe Combe
#id = "544b910d1503dac3318ec7ec" #charlie
#id = "559af7b78c7eee597fd27134" #jenny
#id = "5330eb843ea5c0e3050042c1" #william
#id = "545fb9e33be7f2825978dd57" #john
#id = "56c0782dff767763558964c6" #Laura Voinea
#id = "52ff586a191434912400275a" #aamir
#id = "5525af7c0a76346559bd92d4" #james lynn
#id = "578bee806770910c652b68e7" #george
#id = "54fcdb6431eb40040423a324" # hannah blair
#id = "570d0179036dea490a120d0a" #ankita varsani
#id = "551bc10ece0fb5e917223f54" #barkin celiker
#id = "568a828858d0f4e765bcd8c6" #camille kelly
#id = "541896012d87660c4313d6b5" #darek kargul
#id = "554f5677d3b3f325585bcd3c" #doris nicodei
#id = "52d2a4c2145b76d0370032bf" #fred king
#id = "55b3e8a03163fe484fedbe22" #hannah meyes
#id = "5324d7e8606db6b57a00239b" #jordan king
#id = "53ea0d71345e01d23e0e6071" #jordan mckenzie
#id = "52a95f6114de72d7270001a8" #kat dewar
#id = "5579b12c94f0b1146e5e09f1" #satwick
#id = "535c2880075ae3f0450027b9" #gideon
#id = "5307d8ded14221c32f000308" #jamie davies
#id = "529e4221cb33072d47000024" #kevin lewis
#id = "56158d620c2e5abc065195d3" #ksenia
#id = "57ff8884e130caa535203abb" #sarah elizabeth
#id = "572a98111c59dbfd23f00b15" #vlad
#id = "562eb622e840f50b7b71a7c0"

print "fbtoken is " + str(fbToken) 
base_url = "https://api.gotinder.com/"
recs_endpoint = "user/recs"
loc_endpoint = "user/ping"
friends_endpoint = "group/friends"

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

def test():
    headers = {'Content-Type': 'application/json',
                'User-agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)',
                'app-version': '3',
                'platform' : 'ios',
                'X-Auth-Token': tinder_token,
                'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                }
    r = requests.get(base_url+friends_endpoint, headers = headers)
    #print r.text
    return json.loads(r.text)
#test()

def getUserData(user):
    tinder_headers3 = {'X-Auth-Token': tinder_token,
                       'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore')
                       }
    url3 = 'https://api.gotinder.com/user/{0}'.format(user)
    r3 = requests.get(url3, headers = tinder_headers3)
    #print json.dumps(json.loads(r3.text), indent=4)
    return json.loads(r3.text)

#get_updates()

#def auto_stalk():
#    print test()

#auto_stalk()


def getFriendIDs():
    ids = []
    results = test()
    userids = results["results"]
    for u in userids:
        ids.append(u["user_id"])
        #print u["user_id"]
    return ids

def auto_stalk():
    folder = "fbUsers/"
    sep = "/"
    extension = ".jpg"
    counter = 0
    userImgCount = 0
    smallist = []
    smallist.append(getFriendIDs()[1])
    print smallist[0]
    for friend in getFriendIDs():
        jsonUserData = getUserData(friend)
        name = jsonUserData['results']['name']
        print name
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

