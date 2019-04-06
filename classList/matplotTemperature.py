import matplotlib
matplotlib.use('Agg')
import json
import requests
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector 
import sys

class MatPlotLibTemperature():
 def __init__(self):
  pass

 def outputTemp(self):
   
  #using matplotlib

  #read csv  
  df = pd.read_csv("analytics.csv")
  #plot boxplot for temperature
  df['temperature'].plot(kind = 'box')
  plt.xlabel('Temperature')
  #export image of grpah into file name
  #temperatureBox.png
  plt.savefig('temperatureBox.png')
