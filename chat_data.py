import mysql.connector
from mysql.connector import Error
from database import Data

# La classe Chat interagit avec une base de données de la classe Data :
class Chat(Data):
    def __init__(self):
        Data.__init__(self)
        self.connected()


    def creation_message(self, msg, auteur=1,type=1):
        requete = "INSERT INTO message (message ,auteur,type_message) VALUES (%s, %s, %s)"
        values = (msg,auteur,type)
        self.query(requete,values,modif=True)


    def lecture_message(self):
        requete = "SELECT message FROM message"
        resultat = self.query(requete)
        return resultat
        
    def lecture_time(self): 
        requete = "SELECT time FROM message"
        resultat = self.query(requete)
        return resultat
    
    def id_auteur(self,email):
        requete = "SELECT id FROM user where email=%s"
        value = email
        resultat = self.query(requete,value)
        return resultat
        
    def lecture_id_auteur(self):   
        requete = "SELECT auteur FROM message"
        resultat = self.query(requete,None)
        return resultat
    
    def suppression_message(self, id):
        requete = "DELETE FROM message WHERE id = %s"
        value = (id ,)
        self.query(requete, value, modif = True)
        print("Vous avez supprimé avec succès!") 
                
if __name__ == "__main__":
    chat = Chat()
    # chat.creation_message("Le test à démarré correctement !")
    print(chat.lecture_message())
    # print(chat.id_auteur())
    # print(chat.lecture_id_auteur())
    chat.suppression_message(2)
    