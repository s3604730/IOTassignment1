import json
import logging
#from virtual_sense_hat import VirtualSenseHat
from classList.classTemperature import ClassTemperature 
from classList.classHumidity import ClassHumidity



# the objects with parent abstract class
from classList.classTemperature2 import ClassTemperature2
from classList.classHumidity2 import ClassHumidity2
from classList.classDatabase import Database


#pushbullet utils file
from utils.pushBulletFile import send_notification_via_pushbullet

send_notification_via_pushbullet("fsdfdsaf","fdsfasd")

#date time
from utils.dateTime import getDateTime


#Database
db = Database()
print(db)

#import requests

#initialise database here

#This may not stay in here.

defaultConfig = { "min_temperature" : 20, "max_temperature" : 30, "min_humidity" : 20, "max_humidity" : 60}
#just for creating the json file which is probably not needed

with open('config.json', 'w') as file:
    json.dump(defaultConfig, file, indent=3)

with open("config.json", "r") as file1:
    data = json.load(file1)

print(data)




#get sensor object through abstract class and print value
#temperature
sensorTemperatureObject = ClassTemperature2()
sensorTemperatureValue = sensorTemperatureObject.returnValue()
print(sensorTemperatureValue)

#get sensor object humidity
sensorHumidityObject = ClassHumidity2()
sensorHumidityValue = sensorHumidityObject.returnValue()
print(sensorHumidityValue)


