import csv
import datetime
from classList.Database import Database

with open("report.csv", "w", newline="") as csvfile:
  db = Database()
  res = db.getAllDateData()

  writer = csv.writer(csvfile)
  writer.writerow(["Date", "Status"])

  for x in res:
    status = "OK"
    temp = ""
    humidity= ""

    if(x[1] > 0):
      status = "BAD"
      temp = ": " + str(x[1]) + " *C above maximum temperature"
    elif(x[1] < 0):
      status = "BAD"
      temp = ": " + str(x[1]) + "*C below minimum temperature"
    
    if(x[2] > 0):
      status = "BAD"
      humidity = ": " + str(x[2]) + "'%' above maximum humidity"
    elif(x[2] < 0):
      status = "BAD"
      humidity = ": " + str(x[2]) + "'%' below minimum humidity"

    date = x[3].strftime('%d/%m/%Y')
    writer.writerow([date, status + temp + humidity])