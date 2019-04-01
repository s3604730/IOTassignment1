import mysql.connector
import json
from datetime import datetime

class Database():

  def __init__(self):
    # con = mysql.connector.connect(host="localhost", user="root", password="", database="iot1")
    con = mysql.connector.connect(host="localhost", user="pi1", password="abc123", database="iot1")
    self.cursor = con.cursor()
    self.con = con

  def insertMinData(self, tem, hum):
    stm = ("INSERT INTO recordsByMin(temperature, humidity) VALUES (%s, %s)")

    val = (tem, hum) 

    self.cursor.execute(stm, val)

    self.con.commit()
    
  def insertFirstDateData(self):
    stm = ("INSERT INTO recordsByDate(temperatureExcess, humidityExcess, date, pushed) VALUES (%s, %s, %s, %s)")
    val = (0, 0, datetime.now().strftime('%Y-%m-%d'), False) 

    self.cursor.execute(stm, val)

    self.con.commit()

  def insertDateData(self, tem, hum):
    with open("config.json", "r") as file1:
      data = json.load(file1)
    
    stm = ("UPDATE recordsByDate SET temperatureExcess = %s, humidityExcess = %s, pushed = TRUE WHERE DATE(date) = CURDATE()")

    maxTem = data["max_temperature"]
    minTem = data["min_temperature"]
    maxHum = data["max_humidity"]
    minHum = data["min_humidity"]
    
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

  def readMinData(self):    
    self.cursor.execute("SELECT * FROM recordsByMin")

    res = self.cursor.fetchall()

    for x in res:
      print(x)

  def readDateData(self):
    self.cursor.execute("SELECT * FROM recordsByDate")

    res = self.cursor.fetchall()

    for x in res:
      print(x)
  
  def getAllDateData(self):
    self.cursor.execute("SELECT * FROM recordsByDate")

    res = self.cursor.fetchall()

    return res
    

  def isTodayRecorded(self):
    self.cursor.execute("SELECT * FROM recordsByDate WHERE DATE(date) = CURDATE()")

    res = self.cursor.fetchall()

    return len(res) > 0
  
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
  