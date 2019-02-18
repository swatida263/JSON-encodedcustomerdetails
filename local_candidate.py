from math import radians, cos, sin, asin, sqrt
def haversine(sourceLong, sourceLat, destLong, destLat):
	# convert degrees to radians
	sourceLong, sourceLat, destLong, destLat = map(radians, [sourceLong, sourceLat, destLong, destLat])
	# haversine formula 
	longDistance = destLong - sourceLong 
	latDistance = destLat - sourceLat 
	havTheta = sin(latDistance/2)**2 + cos(sourceLat) * cos(destLat) * sin(longDistance/2)**2
	finalDistance = 2 * asin(sqrt(havTheta)) 
	# Radius of earth = 6371 Km
	distnaceInKm = 6371* finalDistance
	return distnaceInKm

import json
import ast
from pprint import pprint
'''
#Open a json file
with open('/home/soubhagya/Setups/lali/data.json') as f:
	data = json.load(f)
'''
inercomOfficeLong = float(-6.257664)
inercomOfficeLat = float(53.339428)

#Open a text file with dict format
with open('/home/soubhagya/Setups/lali/data.txt') as f:
	#read line by line
	for line in f:
		#Assign each line to a dictionary variable
		dictData = ast.literal_eval(line)
		customerLong = float(dictData['longitude'])
		customerLat = float(dictData['latitude'])
		customerName = dictData['name']
		#Find haversine distance in Km
		haversineDistance = haversine(inercomOfficeLong, inercomOfficeLat, customerLong, customerLat)
		if haversineDistance <= 100:
			print customerName + ' is ' + str(haversineDistance) + ' Km from Dublin office.'

'''
#Logic to process a proper parsable json file
for i in range(1, len(data)):
	long = float(data[i]['longitude'])
	lat = float(data[i]['latitude'])
	customerName = data[i]['name']
	#print long, lat
	km = haversine(float(-6.257664), float(53.339428) , long, lat)
	#print km
	#print type(km)
	if km <= 100:
		print km
		print customerName
'''