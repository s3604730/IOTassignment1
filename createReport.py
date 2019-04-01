import csv
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
      temp = ": " + 
    writer.writerow(["09/03/2019", "OK"])
    writer.writerow(["10/03/2019", "BAD: 5 *C below minimum temperature"])
    writer.writerow(["11/03/2019", "BAD: 10% above maximum humidity"])