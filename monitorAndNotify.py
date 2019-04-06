#!/usr/bin/env python3
import json
import logging
from datetime import datetime
#from virtual_sense_hat import VirtualSenseHat
# from classList.classTemperature import ClassTemperature 
# from classList.classHumidity import ClassHumidity

# the objects with parent abstract class
from classList.Temperature2 import Temperature2

from classList.Humidity2 import Humidity2
from classList.Database import Database 

from utils.pushBulletFile import send_notification_via_pushbullet
import time


#import requests
#initialise database here

#This may not stay in here.

# defaultConfig = { "min_temperature" : 20, "max_temperature" : 30, "min_humidity" : 20, "max_humidity" : 60}
#just for creating the json file which is probably not needed

# with open('config.json', 'w') as file:
#     json.dump(defaultConfig, file, indent=3)

# with open("config.json", "r") as file1:
#     data = json.load(file1)


#get sensor object through abstract class and print value
#temperature
sensorTemperatureObject = Temperature2()
time.sleep(2)
sensorTemperatureValue = sensorTemperatureObject.returnValue()

# #get sensor object humidity
sensorHumidityObject = Humidity2()
sensorHumidityValue = sensorHumidityObject.returnValue()

# #initiate db
db = Database()

# #call db methods
db.insertMinData(sensorTemperatureValue, sensorHumidityValue)
if(db.isTodayRecorded() == False):
  print('today recorded')
  db.insertFirstDateData()

#if temperature or humidity is out of range and there has not been a 
#push notification yet
if((sensorHumidityObject.isOutOfRange() or sensorTemperatureObject.isOutOfRange()) and db.isTodayPushed() == False):
  db.insertDateData(sensorTemperatureValue, sensorHumidityValue)
  
  #if temperature is out of range
  if (sensorTemperatureObject.isOutOfRange()):  
    abc = "Temperature value is " + str(round(sensorTemperatureValue), 1)
    send_notification_via_pushbullet("ALERT", abc)

    #else if humidity is out of range
  elif(sensorHumidityObject.isOutOfRange()):
    abc = "Humidity value is " + str(round(sensorHumidityValue), 1)
    send_notification_via_pushbullet("ALERT", abc)
   
  
  #push notifications here


db.readMinData()
print("----------------")
db.readDateData()