import mysql.connector   #besoins aussi : pip install mysql-connector-python

# cf tutos
#   https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
#   https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa


class Connection:
  def __init__ (self):
    print("init")
  def getConnection(self):
    #print ("debut")
    mydb = mysql.connector.connect(
      host="localhost",
      user='Tristan',#str(input("Identifiant => ")),
      password='Tristan68',#str(input("Mot de passe => ")),
      port=3307,
      charset='utf8',
      database='Pizza'#str(input("Quel DB rejoindre => "))
      #use default port in localhost 3306 => pas besoin de le rajouter*
      # si tu as un container qui tourne avec mapping, le localhost va redireiger vers le container la requete
    )
    print ("tppt")
    return mydb


