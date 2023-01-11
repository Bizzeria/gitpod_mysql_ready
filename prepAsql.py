import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali_definitivo"
    
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY,Nome_proprio VARCHAR(450), razza VARCHAR(450),peso INTEGER,età INTEGER)")


 