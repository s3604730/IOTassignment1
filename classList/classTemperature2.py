from classList.classSensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import json

#using the reference form abstract class ClassSensor
class ClassTemperature2(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        __temperature = __sense.get_temperature()
        return __temperature
    
    @property
    def value(self):
        __sense = VirtualSenseHat.getSenseHat()
        __temperature = __sense.get_temperature()
        return __temperature

    def isOutOfRange(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return self.value < data["min_temperature"] or self.value > data["max_temperature"]