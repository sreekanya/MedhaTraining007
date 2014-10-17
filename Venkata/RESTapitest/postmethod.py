#! /usr/bin/python 

import urllib
import requests

url = "http://medhaws.cloudapp.net:3000/wines"
data = {"name":"TestWine","year":"1548"}
r = requests.post(url,data=data)

