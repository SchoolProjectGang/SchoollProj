import csv
import mysql.connector as sql


with open("./GameList.csv", newline="") as f:
    x = list(csv.reader(f))

db = sql.connect(
    host="localhost", username="yash", password="password123", database="School"
)
cur = db.cursor()
for i in range(len(x) - 1):
    print(i)
    # print(f"insert into Products values('{x[i][0]}', {int(x[i][1])})")
    cur.execute(f'insert into Products values(pid, "{x[i][0]}", {int(x[i][1])})')
db.commit()
print(x)
