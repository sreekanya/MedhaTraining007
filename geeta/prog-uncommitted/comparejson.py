# first getting only keys from json str
import json

with open('ExpectedDataFormat.json') as data_file:
 	data = json.load(data_file)

 	print data[0]
 	for key in data[0]:
 		print key

# now have to match keys in 2 json structures
 