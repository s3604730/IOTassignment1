from classList.classSensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import time

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
