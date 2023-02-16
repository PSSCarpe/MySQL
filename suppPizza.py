from connection import Connection as myConn
import mysql.connector   #besoins aussi : pip install mysql-connector-python


def supp_pizza():
  myConnection  = myConn()
  mydb          = myConnection.getConnection()
  mycursor      = mydb.cursor()

  nom_Pizz      = str(input("Quel est le nom de la pizza à supprimer: "))
  

  # insertCommand  = f"INSERT INTO Ls_Pizza VALUES ('{nom_Pizz}',{prix_Pizz},'{desc_Pizz}', {ajt_pts})"
  # print (" inser = ", insertCommand)
  print("Avant :")
  mycursor.execute("SELECT * FROM Ls_Pizza")
  mydb.commit()
  myresult = mycursor.fetchall()


  mycursor.execute(f"DELETE FROM Ls_Pizza WHERE nom='{nom_Pizz}'")
  mydb.commit()
  myresult = mycursor.fetchall()
  print ("Pizza supprimer!")

  print("Après :")
  mycursor.execute("SELECT * FROM Ls_Pizza")
  mydb.commit()
  myresult = mycursor.fetchall()

  # for x in myresult:
  #   print(x)

supp_pizza()