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
import seaborn as sns



class SeaBornHumidity():
 def __init__(self):
  pass
 #method for outputting graph
 def outputHumidity(self):
 #read csv  
  dff = pd.read_csv("analytics.csv")
  ax = sns.countplot(x = dff['humidity'])
  ax.figure.savefig("humidityBar.png")