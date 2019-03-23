import json
from sense_hat import SenseHat
#import requests

#This may not stay in here.

defaultConfig = { "min_temperature" : 20, "max_temperature" : 30, "min_humidity" : 20, "max_humidity" : 60}
#just for creating the json file which is probably not needed

with open('config.json', 'w') as file:
    json.dump(defaultConfig, file, indent=3)

with open("config.json", "r") as file1:
    data = json.load(file1)

print(data)


#Initilising Sensehat
sense = SenseHat()
sense.clear()

#getting temperature
temp = sense.get_temperature()
print(temp)
humidity = sense.get_humidity()
print(humidity)