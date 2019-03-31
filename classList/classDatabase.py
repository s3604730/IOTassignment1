import mysql.connector

class Database():

  def __init__(self):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="iot1")
    self.cursor = con.cursor()
    self.con = con
  
  def getCon(self):
    return self.con

  def query(self, stm):
    self.cursor.execute(stm)
    return self.cursor.fechone()

  def rows(self):
    return self.cursor.rowcount