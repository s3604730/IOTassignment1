from monitorAndNotify import MonitorAndNotify
sense = MonitorAndNotify.getSenseHat()


#Think about Abstract class then we can
#put parameter of abstract class in this class
class ClassTemperature:
    
        

    def returnCurrentTemperature(self):
        __currentTemperature = sense.get_temperature()
        print(__currentTemperature)
        return __currentTemperature

