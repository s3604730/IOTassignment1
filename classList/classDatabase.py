import mysql.connector


class Database
  dbc = (host="localhost", user="root", password="", database="iot1")

  def __init__(self):
    db = mysql.connect(*self.dbc)
    self.cursor = db.cursor()
  
  def query(self, stm):
    self.cursor.execute(stm)
    return self.cursor.fechone()

  def rows(self):
    return self.cursor.rowcount