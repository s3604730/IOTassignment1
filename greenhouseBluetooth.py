#!/usr/bin/env python3
import bluetooth
import os
import time
from sense_hat import SenseHat
from classList.Humidity import Humidity
from classList.Temperature import Temperature
from utils.bluetoothPush import bluetoothPush
import os
#get relative path
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


# class bluetooth


class greenhouseBluetooth():
    # init
    def __init__(self):

        # search for nearby devices
        self.findNearbyDevices()
        # set name and device to my phone
        user_name = "Tony"
        device_name = "Mi A2 lite"

        self.search(user_name, device_name)
    # see nearby devices

    def findNearbyDevices(self):
        nearbyDevices = bluetooth.discover_devices(lookup_names=True)
        # display nearby devices
        for macAddress, name in nearbyDevices:
            print("Found device with mac-address: " +
                  macAddress + " and name: " + name)
    # method for scanning wh ich calls findNearbyDevices

    def scan(self):
        print("Scanning...")
        self.findNearbyDevices()

        # sleep for 10 seconds
        time.sleep(10)
        # method for searching device with Tony and Mi A2 lite

    def search(self, user_name, device_name):
        while True:
          # if no address
            device_address = None
            dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
            print("\nCurrently: {}".format(dt))
            time.sleep(3)  # Sleep three seconds.
            nearby_devices = bluetooth.discover_devices()
            #loop to find with mac address in array of nearby devices
            for mac_address in nearby_devices:
                if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                    device_address = mac_address
                    break
            #if not empty and found my phone
            if device_address is not None:
                print("Pairing with Tony's phone - Mia A2 lite...")
                print("Hi {}! Your phone ({}) has the MAC address: {}".format(
                    user_name, device_name, device_address))
                #initialise sensehat
                sense = SenseHat()

                temp = Temperature()
                hum = Humidity()
                push = bluetoothPush()
                sense.show_message(
                    "Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
                #create strings
                tempContent = "Current temperature is " + \
                    str(round(temp.returnValue()))
                humContent = "Current humidity is " + \
                    str(round(hum.returnValue()))

                pushContent = tempContent + ' ' + humContent

                if(temp.isOutOfRange()):
                    tempContent += ", which is out of range."
                else:
                    tempContent += ", which is in range."

                if(hum.isOutOfRange()):
                    humContent += ", which is out of range."
                else:
                    humContent += ", which is in range."
                #output message
                abc = tempContent + " " + humContent + " \n" + pushContent
                push.send_notification_via_pushbullet("ALERT", abc)
                # exit program
                break
            else:
                print("Could not find target device nearby...")
                # exit program
                break

#call method
greenhouseBluetooth()
