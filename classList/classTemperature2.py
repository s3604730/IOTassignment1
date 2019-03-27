from classList.classSensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat

#using the reference form abstract class ClassSensor
class ClassTemperature2(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        __temperature = __sense.get_temperature()
        return __temperature