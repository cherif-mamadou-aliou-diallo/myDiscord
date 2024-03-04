from dotenv import load_dotenv
import os 
import mysql.connector
# from mysql.connector import Error

#Chargement des données avecle type d'encodage attribué.
load_dotenv()  

class Data:
    def __init__(self):
        self.__host = os.getenv('host')
        self.__user = os.getenv('user')
        self.__password = os.getenv('password')
        self.__database = os.getenv('database')
        self.mydb = None
        self.cursor = None
         
    def connected(self):    
        '''Connexion à la base de données'''
        
        try:
            self.mydb = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                autocommit=True,
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print(f'Error connection: {err}')

    def query(self,requete,value='',modif=False):
        try:
            # Envoie la requete ("req") à la base de donnée
            self.cursor.execute(requete,value)
            
            # Par défault il fait un fetchall et il retourne le resultat
            if modif is False:
                result = self.cursor.fetchall()
                return result
        except mysql.connector.Error as e:
            # Annule les modifications effectuées
            self.mydb.rollback()
            print(e)
        
    def close(self):  
        # fermeture de la base de donnée.
        self.cursor.close()
        self.mydb.close()


if __name__ == "__main__":
    gestion = Data()
    gestion.connected()
    print(gestion.query('SHOW DATABASES'))
    gestion.close()
    