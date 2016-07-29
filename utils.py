import pprint
import sys
import os
import json
import time
import urllib2
from pprint import pprint
import requests
import datetime
import numpy as np
import re
import glob
import urllib

regexRule = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

def write_file(file, data):
    with open(file, 'w') as outfile:
        outfile.write(data)

def read_file(file):
    with open(file, 'r') as outfile:
        return outfile.read()
        
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None
    
def get_url(line):
    return ''.join(re.findall(regexRule, line))
    