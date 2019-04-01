from classList.Sensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import json

#using the reference from abstract class ClassSensor
class Humidity2(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
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
