import urllib
import urllib2
#import requests

baseURL1="http://medhaws.cloudapp.net:3000/inventory/addItems"
print baseURL1
#baseURL1=baseURL1+"?"+"category="+"testwine"+"&"+"merchantId="+"merchant15"
#f = urllib2.urlopen(baseURL1)			
#data= {"name":"testwine","year":"1560"}
#r = requests.post(baseURL,data=data)

#place POST data in a dictionary
post_data_dictionary = {'category':'testwine','merchantID':'merchant15'}

#encode the POST data to be sent in a URL
post_data_encoded = urllib.urlencode(post_data_dictionary)

#make a request object to hold the POST data and the URL
request_object = urllib2.Request(baseURL1, post_data_encoded)

#make the request using the request object as an argument, store response in a variable
response = urllib2.urlopen(request_object)

#store request response in a string
html_string = response.read()

print html_string

#[content, response_code] = fetch_url(url, params, method)

if (response_code == 200):
  print content
else:
  print response_code