import json
import logging
from datetime import datetime
#from virtual_sense_hat import VirtualSenseHat
# from classList.classTemperature import ClassTemperature 
# from classList.classHumidity import ClassHumidity

# the objects with parent abstract class
from classList.classTemperature2 import ClassTemperature2
from classList.classHumidity2 import ClassHumidity2
from classList.classDatabase import Database 

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
sensorTemperatureObject = ClassTemperature2()
sensorTemperatureValue = sensorTemperatureObject.value

#get sensor object humidity
sensorHumidityObject = ClassHumidity2()
sensorHumidityValue = sensorHumidityObject.value

#initiate db
db = Database()

#call db methods
db.insertMinData(sensorTemperatureValue, sensorHumidityValue)

if((sensorHumidityObject.isOutOfRange() or sensorTemperatureObject.isOutOfRange()) and db.isTodayPushed() == False):
  db.insertDateData(sensorTemperatureValue, sensorHumidityValue)
  #push notifications here



# db.readMinData()
# db.readDateData()