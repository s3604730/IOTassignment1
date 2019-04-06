# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way
from classList.Sensor import ClassSensor
from classList.virtual_sense_hat import VirtualSenseHat
import time
import json
import os

#using the reference form abstract class ClassSensor
class Temperature2(ClassSensor):
    def __init__(self):
        pass
        #abstract method in classSensor
        #returns value of temperature
    def returnValue(self):
        #base temp
        __sense = VirtualSenseHat.getSenseHat()
        time.sleep(3)
        __temperature = __sense.get_temperature()



        #correction temp
        __humidTemp = __sense.get_temperature_from_humidity()
        __pressureTemp = __sense.get_temperature_from_pressure()
        __tempCpu = getCpuTemperature()
        __humid = __sense.get_humidity()
        __pres = __sense.get_pressure()

        #calculating temp with knowledge of 
        #cpu temp

        __temp1 = (__humidTemp + __pressureTemp)/2
        __tempCorrect = __temp1 - ((__tempCpu - __temp1)/ 1.5)
        __tempCorrect = get_smooth(__tempCorrect)
        return __tempCorrect
    
    #out of range check
    def isOutOfRange(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return self.returnValue() < data["min_temperature"] or self.returnValue() > data["max_temperature"]


#getting correction temperature methods

def getCpuTemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))

#average moving
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x

    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3

