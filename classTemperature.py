
from virtual_sense_hat import VirtualSenseHat


#Think about Abstract class then we can
#put parameter of abstract class in this class
class ClassTemperature:
    def __init__(self):
        print("yeet")
         
    def returnCurrentTemperature(self):
     __sense = VirtualSenseHat.getSenseHat()
     __temperature = __sense.get_temperature()
     print(__temperature)
     print ("fdsafads")
     return __temperature

