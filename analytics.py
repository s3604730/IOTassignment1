import matplotlib
matplotlib.use('Agg')
import csv
import datetime
from classList.Database import Database
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector 
from classList.matplotTemperature import MatPlotLibTemperature
from classList.seabornHumidity import SeaBornHumidity
import sys


#open a csv file
with open("analytics.csv", "w", newline="") as csvfile:
 #initialise db
 db = Database()
 #get all the min data records
 res = db.getAllMinData()
 #write to the csv file the header
 writer = csv.writer(csvfile)
 writer.writerow(["temperature", "humidity", "time"])

 #loop through every record and write to the csv 
 #the temp, humidity and time
 for x in res:
  temp = str(x[1])
  humid = str(x[2])
  time = x[3].strftime('%H/%M/%S')
  writer.writerow([temp,humid,time])



#execute method for temp graph with matplotlib
temperatureGraph = MatPlotLibTemperature()
temperatureGraph.outputTemp()



#execute method for humidity graph with seaborn 

humidityGraph = SeaBornHumidity()
humidityGraph.outputHumidity()






