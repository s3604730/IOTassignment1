#!/usr/bin/env python3
# imports
import json
import logging
from datetime import datetime
from classList.Temperature import Temperature
from classList.Humidity import Humidity
from classList.Database import Database
from utils.pushBulletFile import pushBulletFile
import time
import os
os.chdir(r'/home/pi/Assignment1/')


# get temperature
sensorTemperatureObject = Temperature()
sensorTemperatureValue = sensorTemperatureObject.returnValue()

# get humidity
sensorHumidityObject = Humidity()
sensorHumidityValue = sensorHumidityObject.returnValue()

# #initiate db
db = Database()

# call db methods
db.insertMinData(sensorTemperatureValue, sensorHumidityValue)

# if today data is not recorded yet, write the first data to db
# in case temperature and humidity is in range during the whole day
if(db.isTodayRecorded() == False):
    db.insertFirstDateData()


# if temperature or humidity is out of range and there has not been a
# push notification yet
if((sensorHumidityObject.isOutOfRange() or sensorTemperatureObject.isOutOfRange()) and db.isTodayPushed() == False):
    db.insertDateData(sensorTemperatureValue, sensorHumidityValue)

    # Initialise pushbullet
    pushFile = pushBulletFile()

    # if temperature is out of range
    if (sensorTemperatureObject.isOutOfRange()):
        abc = "Temperature value is " + str(round(sensorTemperatureValue, 1))
        pushFile.send_notification_via_pushbullet("ALERT", abc)

        # else if humidity is out of range
    elif(sensorHumidityObject.isOutOfRange()):
        abc = "Humidity value is " + str(round(sensorHumidityValue, 1))
        pushFile.send_notification_via_pushbullet("ALERT", abc)

# log data for testing, will remove for final submission
db.readMinData()
print("----------------")
db.readDateData()
