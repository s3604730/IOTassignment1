import bluetooth
import os
import time
from sense_hat import SenseHat
from classList.Humidity import Humidity
from classList.Temperature import Temperature
from utils.bluetoothPush import bluetoothPush
import os
os.chdir(r'/home/pi/Assignment1/')

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

    temp = Temperature()
    hum = Humidity()
    push = bluetoothPush()
    sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed = 0.05)
    
    tempContent = "Current temperature is " + str(round(temp.returnValue()))
    humContent = "Current humidity is " + str(round(hum.returnValue()))

    pushContent = tempContent + ' ' + humContent
    # pushbullet here
    push.send_notification_via_pushbullet("ALERT", pushContent)



    if(temp.isOutOfRange()):
     tempContent += ", which is out of range."
    else:
     tempContent += ", which is in range."
    
    if(hum.isOutOfRange()):
     humContent += ", which is out of range."
    else:
     humContent += ", which is in range."

    abc = tempContent + " " + humContent
    push.send_notification_via_pushbullet("ALERT", abc)
   
    #sleep for a minute to stop spamming
    time.sleep(60)
   else:
    print("Could not find target device nearby...")

greenhouseBluetooth()