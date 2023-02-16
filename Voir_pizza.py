from connection import Connection as myConn
import mysql.connector   #besoins aussi : pip install mysql-connector-python

def voir_pizza():
  myConnection  = myConn()
  mydb          = myConnection.getConnection()
  mycursor      = mydb.cursor()
  
  print ("Voici la liste des pizzas :")
  mycursor.execute("SELECT * FROM Ls_Pizza")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

voir_pizza()