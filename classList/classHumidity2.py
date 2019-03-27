from classList.classSensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat


class ClassHumidity2(ClassSensor):
    def __init__(self):
        pass

    def returnValue(self):
        __sense = VirtualSenseHat.getSenseHat()
        __humidity = __sense.get_humidity()
        return __humidity
