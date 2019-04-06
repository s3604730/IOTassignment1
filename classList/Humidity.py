from classList.Sensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import time
import json

#using the reference from abstract class ClassSensor
class Humidity(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        time.sleep(2)
        __humidity = __sense.get_humidity()
        
        return __humidity
    
    def isOutOfRange(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return self.returnValue() < data["min_humidity"] or self.returnValue() > data["max_humidity"]