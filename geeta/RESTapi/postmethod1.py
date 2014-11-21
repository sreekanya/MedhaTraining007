# script working...posting new data to 

#! /usr/bin/python 

import urllib
import requests

url = "http://medhaws.cloudapp.net:3000/wines"
data = {"year":"1200","name":"Clos de Tart","Country":"North America","description":"Cognac"}
r = requests.post(url,data=data)