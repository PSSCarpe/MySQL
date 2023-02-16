import mysql.connector   #besoins aussi : pip install mysql-connector-python

# cf tutos
#   https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
#   https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa


mydb = mysql.connector.connect(
  host="localhost",
  user="Tristan",
  password="Tristan68",
  port=3307,
  database="Pizza"
  #use default port in localhost 3306 => pas besoin de le rajouter*
  # si tu as un container qui tourne avec mapping, le localhost va redireiger vers le container la requete
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from Ls_Pizza")
myresult = mycursor.fetchall()
#print ("Affichage resultat")
for x in myresult:
  print(x)

