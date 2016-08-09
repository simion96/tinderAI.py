import requests
import utils as utils
import json

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
id = "559af7b78c7eee597fd27134" #jenny
#id = "5330eb843ea5c0e3050042c1" #william
#id = "545fb9e33be7f2825978dd57" #john
#id = "56c0782dff767763558964c6" #Laura Voinea
#id = "52ff586a191434912400275a" #aamir
#id = "5525af7c0a76346559bd92d4" #james lynn
#id = "578bee806770910c652b68e7" #george

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



