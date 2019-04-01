from classList.virtual_sense_hat import VirtualSenseHat


#Think about Abstract class then we can
#put parameter of abstract class in this class
class Temperature:
    def __init__(self):
        pass
         
    #abstract class of returnValue??
    def returnCurrentTemperature(self):
     __sense = VirtualSenseHat.getSenseHat()
     __temperature = __sense.get_temperature()

     return __temperature

