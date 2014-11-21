#! /usr/bin/python
import urllib2

import requests
#import json

url="http://medhaws.cloudapp.net:3000/wines"

data={"name":"Clos de Tart trial","Country":"North America"}

r=requests.post(url,data=data)

# this is working...posting the data