import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali_definitivo"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
val = [
    ("Claudio", "Cane", 20, 5),
    ("rick", "gatto", 7, 6),
    ("anna", "canguro", 50, 6),
    ("Marco", "topo", 1, 2),
    ("brick", "rana", 1, 4)
]
mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "was inserted")

