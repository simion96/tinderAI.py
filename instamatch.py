from random import uniform
from math import fabs
import random
import utils as utils
import requests
import json
print ("hey")
currentLoc = [51.065812, -0.335402]
lowerLimit = 0.005
idealLimit = 0.05
upperLimit = 0.075
#0.000100, 0.000100 diff - couple of houses away
#51.065000, -0.335000, 51.065999, -0.335999 100m
#51.060000, -0.330000, 51.069999, -0.339999 3.15km
#51.030000, -0.300000, 51.039999, -0.399999 7.9km

config = utils.read_file('CONFIG.cfg').splitlines()
fbToken = config[0]  
fbID = config[1]     
print ("fbtoken is " + str(fbToken)) 

base_url = "https://api.gotinder.com/"
recs_endpoint = "user/recs/"


def initialize():
    url = 'https://api.gotinder.com/auth'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder/4.8.2 (iPhone; iOS 9.1; Scale/2.00)'}
    payload = {'force_refresh': 'False', 'facebook_id': fbID, 'facebook_token': fbToken}
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    #print r.text
    rjson = json.loads(r.text)
    print ("token is: " + rjson['token'])
    return rjson['token']

tinder_token = initialize()

#while true:
#dps = []
#for i, c in enumerate(currentLoc):
#    dps.append(c.split(".")[1])
    #065812, 335402
#while dps[0] > 
#while True:

lng = []
lat = []
newLoc = []



def getNewLocation():
    tmpLoc = []
    while True:
        if (random.choice([True, False]) == True):
            tmpLoc = [uniform(currentLoc[0], currentLoc[0]+upperLimit), uniform(currentLoc[1], currentLoc[1]+upperLimit)]
        else:
            tmpLoc = [uniform(currentLoc[0], currentLoc[0]-upperLimit), uniform(currentLoc[1], currentLoc[1]-upperLimit)]
        #get random location
        
        if (fabs(tmpLoc[0] - currentLoc[0]) > lowerLimit) and (fabs(tmpLoc[1] - currentLoc[1]) < upperLimit):
            return tmpLoc
            #yield tmpLoc[0]
            #yield tmpLoc[1]
             #if 

def changeLoc():
    values = getNewLocation()
    tmplng = values[0]
    tmplat = values[1]
    if not(tmplng in lng) and not(tmplat in lat):
        lng.append(tmplng)
        lat.append(tmplat)
        print ("{} {}".format(lng[0], lat[0]))
        print (len(lng))
    

#getting reccomandations
def get_recs():
    tinder_headers = {'X-Auth-Token': tinder_token,
                      'Authorization': 'Token token="{0}"'.format(tinder_token).encode('ascii', 'ignore'),
                       'locale': 'en-GB'
                      }
    r = requests.post(base_url+recs_endpoint, headers = tinder_headers)
    with open('data.txt', 'w') as outfile:
        json.dump(r.text, outfile, sort_keys=True, indent=4)
    with open('data.txt') as data_file:
        recs_json = json.load(data_file)
    recs_json2 = utils.byteify(recs_json)
    print (r.url)
    print (r.headers)
    print (r.request)
    print (r.status_code)
    dict = json.loads(recs_json2)
    return dict['results']

def __main__():
#def match():
while True:
    changeLoc()
#curLocDec = float(currentLoc[0])
#print(str(curLocDec[0]))
