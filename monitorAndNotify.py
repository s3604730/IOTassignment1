import json
from sense_hat import SenseHat
import logging
from virtual_sense_hat import VirtualSenseHat
from classTemperature import ClassTemperature

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

def getDataSenseHat():
    sense = VirtualSenseHat.getSenseHat()
    temperature = sense.get_temperature()
    print(temperature)


getDataSenseHat()
yes = ClassTemperature()
print(yes.returnCurrentTemperature())

"""
#Initilising Sensehat
sense = SenseHat()
sense.clear()

#getting temperature
temp = sense.get_temperature()
print(temp)

#getting humid
humidity = sense.get_humidity()
print(humidity)
"""

        