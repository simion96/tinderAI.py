import requests
import urllib2
import httplib
import json


access_token = "2260798150.5029a98.aa136b2cc1aa4367b51e8ce753f1e308"
#r = requests.get("https://instagram.com/oauth/authorize/?client_id=5029a98b04474633aae46fffe2d8e6c6&redirect_uri=http://localhost:6379/oauth_callback&response_type=token")
#print r.text
#print r.url

r = requests.get("https://api.instagram.com/v1/users/search?q=laura&access_token=2260798150.5029a98.aa136b2cc1aa4367b51e8ce753f1e308")
print r.text
print r.text[3]
out = json.loads(r.text)
#print out['data'][0]['username']
print out



# req = urllib2.urlopen("https://instagram.com/oauth/authorize/?client_id=5029a98b04474633aae46fffe2d8e6c6&redirect_uri=http://localhost:6379/oauth_callback&response_type=token")
# print req.geturl()
# print req.info()
# print req.response.read()


#2260798150.5029a98.aa136b2cc1aa4367b51e8ce753f1e308