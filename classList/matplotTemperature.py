import mysql.connector
import sys
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
import requests
import json
import matplotlib
matplotlib.use('Agg')


class MatPlotLibTemperature():
    def __init__(self):
        pass

    def outputTemp(self):

        # using matplotlib

        # read csv
        df = pd.read_csv("analytics.csv")
        # plot boxplot for temperature
        df['temperature'].plot(kind='box')
        # export image of grpah into file name
        # temperatureBox.png
        plt.savefig('temperatureBox.png')
