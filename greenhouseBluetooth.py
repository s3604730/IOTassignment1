import bluetooth
import os
import time
from sense_hat import SenseHat
from classList.Humidity2 import Humidity2
from classList.Temperature2 import Temperature2
from utils.pushBulletFile import send_notification_via_pushbullet

class greenhouseBluetooth():
 def __init__(self):
  print("Scanning...")
  self.findNearbyDevices()
  user_name = "Tony"
  device_name = "Mi A2 lite"
  self.search(user_name, device_name)

 def findNearbyDevices(self):
  nearbyDevices = bluetooth.discover_devices(lookup_names=True)

  for macAddress, name in nearbyDevices:
   print("Found device with mac-address: " + macAddress + " and name: " + name)

 def scan(self):
  print("Scanning...")
  self.findNearbyDevices();

  print("Sleeping for 10 seconds.")
  time.sleep(10)

 def search(self, user_name, device_name):
  while True:
   device_address = None
   dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
   print("\nCurrently: {}".format(dt))
   time.sleep(3) # Sleep three seconds.
   nearby_devices = bluetooth.discover_devices()

   for mac_address in nearby_devices:
    if device_name == bluetooth.lookup_name(mac_address, timeout = 5):
     device_address = mac_address
     break
   if device_address is not None:
    print("Pairing with Tony's phone - Mia A2 lite...")
    print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
    sense = SenseHat()

    temp = Temperature2();
    hum = Humidity2();
    sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed = 0.05)
    # pushbullet here
    tempContent = "Current temperature is " + str(temp.returnValue())
    humContent = "Current humidity is " + str(hum.returnValue())

    if(temp.isOutOfRange()):
     tempContent += ", which is out of range."
    else:
     tempContent += ", which is in range."
    
    if(hum.isOutOfRange()):
     humContent += ", which is out of range."
    else:
     humContent += ", which is in range."

    abc = tempContent + " " + humContent
    send_notification_via_pushbullet("ALERT", abc)
   else:
    print("Could not find target device nearby...")

greenhouseBluetooth()