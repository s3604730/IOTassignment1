from classList.Sensor import Sensor
from classList.virtual_sense_hat import VirtualSenseHat
import time
import json

#using the reference from abstract class ClassSensor
class ClassHumidity2(ClassSensor):
    def __init__(self):
        pass
    #abstract method in classSensor
    #returns value of humidity
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        time.sleep(1)
        __humidity = __sense.get_humidity()
        
        return __humidity
    
    @property
    def value(self):
        __sense = VirtualSenseHat.getSenseHat()
        __humidity = __sense.get_humidity()
        return __humidity

    def isOutOfRange(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return self.value < data["min_humidity"] or self.value > data["max_humidity"]
