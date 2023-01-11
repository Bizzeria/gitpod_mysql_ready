import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali_definitivo"
)

mycursor = mydb.cursor()

n_volte= int(input("Quanti animali si vuole inserire? "))
for x in range (n_volte):
    nome= str(input("Digitare il nome dell'animale: "))
    razza= str(input("Digitare la razza dell'animale: "))
    peso = int(input("Digitare il peso dell'animale: "))
    età= int(input("Digitare l'età dell'animale: "))  
    sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
    val = (nome, razza , peso , età)
    
    mycursor.execute(sql,val)

    mydb.commit()

    print("animale inserito")

