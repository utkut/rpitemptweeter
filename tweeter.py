#!/usr/bin/python

# Author: Utku Tarhan

# Requires https://github.com/adafruit/Adafruit_Python_BMP to be installed with twython package which could be installed: sudo pip install twython

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
import time
from twython import Twython
# your twitter access information goes here

apiKey = 'REPLACEME'
apiSecret = 'REPLACEME'
accessToken = 'REPLACEME'
accessTokenSecret = 'REPLACEME'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Importing the BMP library
import Adafruit_BMP.BMP085 as BMP085

# Creating an 'object' containing the BMP180 data
bmp = BMP085.BMP085()

# Attempt to get sensor readings.
temp = bmp.read_temperature()
pressure = bmp.read_pressure()
altitude = bmp.read_altitude()

print 'Temperature: {0:0.1f} C'.format(temp)
print 'Pressure:    {0:0.1f} Pa'.format(pressure)
print 'Altitude:    {0:0.1f} m'.format(altitude)

api.update_status(status='Temp = {0:0.2f} *C'.format(temp)+ '  ' + 'Pressure = {0:0.2f} Pa'.format(pressure)+ '  ' + 'Altitude = {0:0.2f} m'.format(altitude))
