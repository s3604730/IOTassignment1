import json
import logging
#from virtual_sense_hat import VirtualSenseHat
from classList.classTemperature import ClassTemperature 
from classList.classHumidity import ClassHumidity

from classList.classTemperature2 import ClassTemperature2

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

#Initialise object with getting Temperature and humidity
# with abstract class, we may not need to call it twice

sensorTemperature = ClassTemperature()
sensorHumidity = ClassHumidity() 
print(sensorTemperature.returnCurrentTemperature())
print(sensorHumidity.returnCurrentHumidity())
print("fdsaf")

sensorTemperatureObject = ClassTemperature2()
sensorTemperatureValue = sensorTemperatureObject.returnValue()
print(sensorTemperatureValue)