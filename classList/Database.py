import mysql.connector
import json
from datetime import datetime

class Database():

  def __init__(self):
    # mysql config of Pi
    con = mysql.connector.connect(host="localhost", user="pi1", password="abc123", database="iot1")
    self.cursor = con.cursor()
    self.con = con

  # insert minute data method
  def insertMinData(self, tem, hum):
    stm = ("INSERT INTO recordsByMin(temperature, humidity) VALUES (%s, %s)")

    val = (tem, hum) 

    self.cursor.execute(stm, val)

    self.con.commit()

  # insert the first data for date to determine if temperature and humidity is in range the whole day or just the Pi is not used  
  def insertFirstDateData(self):
    stm = ("INSERT INTO recordsByDate(temperatureExcess, humidityExcess, date, pushed) VALUES (%s, %s, %s, %s)")
    val = (0, 0, datetime.now().strftime('%Y-%m-%d'), False) 

    self.cursor.execute(stm, val)

    self.con.commit()

  # insert data for date if temperature and humidity is out of range (only once per day)
  def insertDateData(self, tem, hum):
    with open("config.json", "r") as file1:
      data = json.load(file1)
    
    stm = ("UPDATE recordsByDate SET temperatureExcess = %s, humidityExcess = %s, pushed = TRUE WHERE DATE(date) = CURDATE()")

    maxTem = data["max_temperature"]
    minTem = data["min_temperature"]
    maxHum = data["max_humidity"]
    minHum = data["min_humidity"]
    # calculate temperature and humidity excesses
    temExcess = 0
    humExcess = 0

    if(tem > maxTem):
      temExcess = tem - maxTem
    
    if(tem < minTem):
      temExcess = tem - minTem

    if(hum > maxHum):
      humExcess = hum - maxHum
    
    if(hum < minHum):
      humExcess = hum - minHum
    
    val = (temExcess, humExcess) 

    self.cursor.execute(stm, val)

    self.con.commit()

  # log data from recordsByMin table
  def readMinData(self):    
    self.cursor.execute("SELECT * FROM recordsByMin")

    res = self.cursor.fetchall()

    for x in res:
      print(x)

  # log data from recordsByDate table
  def readDateData(self):
    self.cursor.execute("SELECT * FROM recordsByDate")

    res = self.cursor.fetchall()

    for x in res:
      print(x)
  
  # get all data from recordsByDate table
  def getAllDateData(self):
    self.cursor.execute("SELECT * FROM recordsByDate")

    res = self.cursor.fetchall()

    return res

  # get all data from recordsByMin table
  def getAllMinData(self):
    self.cursor.execute("SELECT * FROM recordsByMin")

    res = self.cursor.fetchall()

    return res
    
  # this method is used to determine if the Pi is booted during the day or not
  # also used to write the first data for date table
  def isTodayRecorded(self):
    self.cursor.execute("SELECT * FROM recordsByDate WHERE DATE(date) = CURDATE()")

    res = self.cursor.fetchall()

    return len(res) > 0
  
  # this method is used to determine if temperature or humidity value is out of range during the day or not.
  # also used to determine if notification has been sent today or not.
  def isTodayPushed(self):
    self.cursor.execute("SELECT * FROM recordsByDate WHERE DATE(date) = CURDATE()")

    res = self.cursor.fetchall()

    if(len(res) == 0):
      return False
    else:
      for x in res:
        if(x[4] == False):
          return False
      return True
  