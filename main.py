from findTotalMales import findTotalMales
from deg2rad import deg2rad
import argparse
import numpy as np
import itertools as it
from dataVector import fixData

#dataset = np.genfromtxt('age_data.csv', delimiter=',', skip_header=1)

long1 = np.arange(69.35, 70.8, .01)
lat = np.arange(43, 44.45, .01)
#longitude_raw = dataset[:, 1]
#latitude_raw = dataset[:, 2]
#totmale_all_raw = dataset[:, 15]

longitude_raw = (70.8 - 69.35) * np.random.random(1000) + 69.35
latitude_raw = (44.45 - 43) * np.random.random(1000) + 43
totmale_all_raw = np.random.random(1000)

long_grid, lat_grid, long_test, lat_test, data_test = fixData(long1, lat, longitude_raw, latitude_raw, totmale_all_raw)

rEarth = 6371e3
phi1 = deg2rad(lat_grid)
phi2 = deg2rad(lat_test)
deltaPhi = deg2rad(lat_test - lat_grid)
deltaLambda = deg2rad(long_test	- long_grid)

a = np.sin(deltaPhi/2) * np.sin(deltaPhi/2) \
	+ np.cos(phi1) * np.cos(phi2) * np.sin(deltaLambda/2) * np.sin(deltaLambda/2)
c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
d = rEarth * c

#long_repeat = np.repeat(long, len(lat))
#lat_repeat = np.tile(lat, len(long))
#splitLat = np.split(lat_repeat, 2)
#splitLong = np.split(long_repeat, 2)

#grid = np.array([long_repeat, lat_repeat])
#maxMen = 0
#print grid

#print findTotalMales(1.609, np.split(lat_repeat, 2)[0], np.split(long_repeat, 2)[0], dataset)
#print findTotalMales(1.609, np.split(lat_repeat, 2)[1], np.split(long_repeat, 2)[1], dataset)

#sums1, lat1, long1 = findTotalMales(1.609, splitLat[0], splitLong[0], dataset)
#sums2, lat2, long2 = findTotalMales(1.609, splitLat[1], splitLong[1], dataset)

#print 'totMale, latitude, longitude'

#for x, y, z in it.izip(sums1, lat1, long1):
#	print str(x) + ', ' + str(y) + ', ' + str(-1*z)

#for x, y, z in it.izip(sums2, lat2, long2):
#	print str(x) + ', ' + str(y) + ', ' + str(-1*z)

#for x in long:
#	for y in lat:
#		tempMax = findTotalMales(40, y, x, dataset)
#		if tempMax > maxMen:
#			maxMen = tempMax
#			maxLat = y
#			maxLong = x
#
#print maxMen, maxLat, -maxLong