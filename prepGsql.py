import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali_definitivo"
)

mycursor = mydb.cursor()

print("Premi 1 per inserire un nuovo animale", "")
print("Premi 2 per visualizzare tutti gli animali", "")
print("Premi 3 per eliminare un animale", "")
print("Premi 4 per modificare un animale", "")
n= int(input(""))
if n == 1:
    nome= str(input("Digitare il nome dell'animale: "))
    razza= str(input("Digitare la razza dell'animale: "))
    peso = int(input("Digitare il peso dell'animale: "))
    età= int(input("Digitare l'età dell'animale: "))  
    sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
    val = (nome, razza , peso , età)
    
    mycursor.execute(sql,val)

    mydb.commit()

    print("animale inserito")
elif n == 2: 
    mycursor.execute("SELECT * FROM Mammiferi")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
elif n == 3:
    sacrificio = (input("Digitare l'id dell'animale da eliminare: "))
    sql = "DELETE FROM Mammiferi WHERE id = %s"

    val= (sacrificio,)
    sql2 = "SELECT id FROM Mammiferi WHERE id = %s"
    val2 = [sacrificio]

    mycursor.execute(sql2,val2)
    myresult = mycursor.fetchone()
    if myresult == None:
        print("non esistono animali con quell'id")
    else:
        mycursor.execute(sql,val)
        mydb.commit()
        print("animale eliminato")
elif n == 4:
    sacrificio = (input("Digitare l'id dell'animale da modificare: "))
    sql = "DELETE FROM Mammiferi WHERE id = %s"

    val= (sacrificio,)
    sql2 = "SELECT id FROM Mammiferi WHERE id = %s"
    val2 = [sacrificio]

    mycursor.execute(sql2,val2)
    myresult = mycursor.fetchone()
    if myresult == None:
        print("non esistono animali con quell'id")
    else:
        mycursor.execute(sql,val)
        mydb.commit()
        nome= str(input("Digitare il nome dell'animale: "))
        razza= str(input("Digitare la razza dell'animale: "))
        peso = int(input("Digitare il peso dell'animale: "))
        età= int(input("Digitare l'età dell'animale: "))  
        sql3 = "INSERT INTO Mammiferi (id, Nome_proprio, Razza, peso, età) VALUES (%s,%s, %s, %s, %s)"
        val3 = (sacrificio, nome, razza , peso , età)
    
        mycursor.execute(sql3,val3)

        mydb.commit()

        print("animale modificato")
