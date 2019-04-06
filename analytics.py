import matplotlib
matplotlib.use('Agg')
import csv
import datetime
from classList.Database import Database
import pandas as pd
import matplotlib.pyplot as plt

import mysql.connector 

import sys

with open("analytics.csv", "w", newline="") as csvfile:
 db = Database()

 res = db.getAllMinData()

 writer = csv.writer(csvfile)
 writer.writerow(["temperature", "humidity", "time"])


 for x in res:
  temp = str(x[1])
  humid = str(x[2])
  time = x[3].strftime('%H/%M/%S')
  writer.writerow([temp,humid,time])




 #using matplotlib

  
df = pd.read_csv("analytics.csv")
df['temperature'].plot(kind = 'box')
plt.xlabel('Temperature')
plt.savefig('temperatureBox.png')

