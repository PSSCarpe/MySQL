from connection import Connection as myConn
import mysql.connector   #besoins aussi : pip install mysql-connector-python


def inser_pizza():
  myConnection  = myConn()
  mydb          = myConnection.getConnection()
  mycursor      = mydb.cursor()

  nom_Pizz      = str(input("Quel est le nom de la nouvelle pizza : "))
  prix_Pizz     = float(input("Quel est le prix de la nouvelle pizza : "))
  desc_Pizz     = str(input("Quel est la description de la nouvelle pizza : "))

  if prix_Pizz >= 11:
    ajt_pts = 2
  else:
    ajt_pts = 1


  # insertCommand  = f"INSERT INTO Ls_Pizza VALUES ('{nom_Pizz}',{prix_Pizz},'{desc_Pizz}', {ajt_pts})"
  # print (" inser = ", insertCommand)
  print("Avant :")
  mycursor.execute("SELECT * FROM Ls_Pizza")
  mydb.commit()
  myresult = mycursor.fetchall()

  mycursor.execute(f"INSERT INTO Ls_Pizza VALUES ('{nom_Pizz}',{prix_Pizz},'{desc_Pizz}', {ajt_pts})")
  mydb.commit()
  myresult = mycursor.fetchall()
  print ("Pizza insérée!")

  print("Après :")
  mycursor.execute("SELECT * FROM Ls_Pizza")
  mydb.commit()
  myresult = mycursor.fetchall()

  # for x in myresult:
  #   print(x)

inser_pizza()