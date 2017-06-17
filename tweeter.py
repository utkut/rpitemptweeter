#!/usr/bin/python

import sys
import os
import time
from twython import Twython
CONSUMER_KEY = 'SECRET'
CONSUMER_SECRET = 'SECRET'
ACCESS_KEY = 'SECRET'
ACCESS_SECRET = 'SECRET'

# your twitter access information goes here

apiKey = 'REPLACETHECODE'
apiSecret = 'REPLACETHECODE'
accessToken = 'REPLACETHECODE'
accessTokenSecret = 'REPLACETHECODE'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Importing the BMP library
import Adafruit_BMP.BMP085 as BMP085 

# Creating an 'object' containing the BMP180 data
sensor = BMP085.BMP085()

# Attempt to get sensor readings.
temp = bmp.read_temperature()
pressure = bmp.read_pressure()
altitude = bmp.read_altitude()

print 'Temperature: {0:0.1f} C'.format(temp)
print 'Pressure:    {0:0.1f} Pa'.format(pressure)
print 'Altitude:    {0:0.1f} m'.format(altitude)

	api.update_status(status=temp+pressure+altitude)


	time.sleep(1800)

