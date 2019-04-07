import mysql.connector
import seaborn as sns
import sys
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
import requests
import json
import matplotlib
matplotlib.use('Agg')


class SeaBornHumidity():
    def __init__(self):
        pass
    # method for outputting graph

    def outputHumidity(self):
        # read csv
        dff = pd.read_csv("analytics.csv")
        ax = sns.countplot(x=dff['humidity'])
        ax.figure.savefig("humidityBar.png")
