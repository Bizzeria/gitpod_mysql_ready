import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali_definitivo"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi WHERE peso > 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)