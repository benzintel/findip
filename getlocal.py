import urllib2
import json
import requests

fr = open('ip_list.txt', 'r')
fw = open('output.txt', 'w')
for x in fr:
	url = "http://freegeoip.net/json/" + x.rstrip()
	data = urllib2.urlopen(url).read()
	city =  json.loads(data)['city']
	region_name = json.loads(data)['region_name']
	if city == '':
		out = x.rstrip() + ',unknown,' + region_name + ',\n'
	else:
		out = x.rstrip() + ',' + city + ',' + region_name + ',\n'
	print out
	fw.write(out)