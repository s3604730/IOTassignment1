from classList.virtual_sense_hat import VirtualSenseHat

#think about putting abstract class later on

class Humidity:
    def __init__(self):
        pass

    #abstract class of returnValue 
    #similar to temperature???
    def returnCurrentHumidity(self):
        __sense = VirtualSenseHat.getSenseHat()
        __humidity = __sense.get_humidity()
        print(__humidity)
        print("Fdsfsadfsadf")
        return __humidity