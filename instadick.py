import requests
import urllib2
import httplib
import json


access_token = "2260798150.5029a98.aa136b2cc1aa4367b51e8ce753f1e308"
r = requests.get("https://api.instagram.com/v1/users/search?q=laura&access_token=2260798150.5029a98.aa136b2cc1aa4367b51e8ce753f1e308")
out = json.loads(r.text)