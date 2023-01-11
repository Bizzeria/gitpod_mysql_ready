import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali_definitivo"
)

mycursor = mydb.cursor()

nuovo1 = str(input("Inserire un animale? (minuscolo): "))
if nuovo1 == "si":
    nome1= str(input("Digitare il nome dell'animale: "))
    razza1= str(input("Digitare la razza dell'animale: "))
    peso1= int(input("Digitare il peso dell'animale: "))
    età1= int(input("Digitare l'età dell'animale: "))  
    sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
    val = (nome1, razza1 , peso1 , età1)
    
    mycursor.execute(sql,val)

    mydb.commit()

    print("animale inserito")  
    nuovo2 = str(input("Inserire un animale? (minuscolo): "))
    if nuovo2 == "si":
        nome2= str(input("Digitare il nome dell'animale: "))
        razza2= str(input("Digitare la razza dell'animale: "))
        peso2= int(input("Digitare il peso dell'animale: "))
        età2= int(input("Digitare l'età dell'animale: "))  
        sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
        val = (nome2, razza2 , peso2 , età2)
    
        mycursor.execute(sql,val)

        mydb.commit()

        print("animale inserito")
        nuovo3 = str(input("Inserire un animale? (minuscolo): "))
        if nuovo3 == "si":
            nome3= str(input("Digitare il nome dell'animale: "))
            razza3= str(input("Digitare la razza dell'animale: "))
            peso3= int(input("Digitare il peso dell'animale: "))
            età3= int(input("Digitare l'età dell'animale: "))  
            sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
            val = (nome3, razza3 , peso3 , età3)
    
            mycursor.execute(sql,val)

            mydb.commit()

            print("animale inserito")
            nuovo4 = str(input("Inserire un animale? (minuscolo): "))
            if nuovo4 == "si":
                nome4= str(input("Digitare il nome dell'animale: "))
                razza4= str(input("Digitare la razza dell'animale: "))
                peso4= int(input("Digitare il peso dell'animale: "))
                età4= int(input("Digitare l'età dell'animale: "))  
                sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
                val = (nome4, razza4 , peso4 , età4)

                mycursor.execute(sql,val)

                mydb.commit()

                print("animale inserito")
                nuovo5 = str(input("Inserire un animale? (minuscolo): "))
                if nuovo5 == "si":
                    nome5= str(input("Digitare il nome dell'animale: "))
                    razza5= str(input("Digitare la razza dell'animale: "))
                    peso5= int(input("Digitare il peso dell'animale: "))
                    età5= int(input("Digitare l'età dell'animale: "))  
                    sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, peso, età) VALUES (%s, %s, %s, %s)"
                    val = (nome5, razza5 , peso5 , età5)

                    mycursor.execute(sql,val)

                    mydb.commit()

                    print("animale inserito")
