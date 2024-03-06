# Importe la fonction load_dotenv de la bibliothèque dotenv.
from dotenv import load_dotenv
#  Un module Python pour interagir avec le système d'exploitation, utilisé ici pour accéder aux variables d'environnement chargées
import os 
# Un module Python pour interagir avec des bases de données MySQL
import mysql.connector
#  Une classe d'erreur spécifique fournie par mysql.connector.
from mysql.connector import Error


# utilisée pour charger les variables d'environnement depuis un fichier .env.
load_dotenv(encoding="utf-8")  

# La classe Data permet d'intéragir avec la base de donnée interagir avec une base de données.
class Data:
    # Initialise les variables privées pour stocker les informations de la base de données à partir des variables d'environnement.
    def __init__(self):
        #self.__host = os.getenv('host')
        #self.__user = os.getenv('user')
        #self.__password = os.getenv('password')
        #self.__database = os.getenv('database')
        self.__host = 'localhost'
        self.__user = 'root'
        self.__password = '0000'
        self.__database = 'discord'
        #self.mydb = None
        #self.cursor = None
        # La méthode connected() établit une connexion à la base de données en utilisant les informations d'identification récupérées.
    def connected(self):    
        '''Connexion à la base de données'''
        # Gestion des exceptions :
        # Si la connexion échoue pour une raison quelconque alors l'erreur sera capturé dans le bloc except.
        try:
            self.mydb = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                autocommit=True,
                #auth_plugin='mysql_native_password'
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print(f'Error connection: {err}')
            
    # La méthode query exécute une requête SQL sur la base de données. 
    # pour effectuer des modifications (modif=True) 
    # ou récupérer des résultats (modif=False).
    # value est initialisée avec la valeur spéciale None.
    def query(self,requete,value=None,modif=False):
        
        try:
            # Envoie la requete ("req") à la base de donnée.
            self.cursor.execute(requete,value)
            # modif = True signifie que la méthode ne retournera rien et par défaut False.
            if modif is False: #  l'utilisateur souhaite récupérer les résultats d'une requête SQL sans effectuer de modifications dans la base de données.
                result = self.cursor.fetchall() # est utilisée pour récupérer toutes les lignes de résultats d'une requête SQL exécutée à l'aide d'un curseur dans Python.
                return result
                
        except mysql.connector.Error as e:
            # Annule les modifications effectuées
            self.mydb.rollback()
            print(e) # affichage de l'erreur
        
        # fermeture de la base de donnée.
    def close(self):  
        self.cursor.close() # self.cursor.close ferme le curseur associé à la connexion à la base de données.
        self.mydb.close() # self.mydb.close de code ferme la connexion à la base de données elle-même. 


if __name__ == "__main__":
    gestion = Data()
   
    gestion.connected()
    print(gestion.query('SELECT message FROM message'))
    # gestion.close()