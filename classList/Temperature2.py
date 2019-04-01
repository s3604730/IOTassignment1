from classList.Sensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import time
import json

#using the reference form abstract class ClassSensor
class Temperature2(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
        #returns value of temperature
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        time.sleep(1)
        __temperature = __sense.get_temperature()
        return __temperature
    
    def isOutOfRange(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return self.returnValue() < data["min_temperature"] or self.returnValue() > data["max_temperature"]