# read response data
import urllib2
import re
import json
import sys
from pprint import pprint 
import os

with open('ExpectedDataFormat.json') as data1_file:
 	data1 = json.load(data1_file)