import mysql.connector
from mysql.connector import Error
from database import Data

class Chat(Data):
    def __init__(self):
        self.data = Data()


    def creation_message(self, msg, type,auteur):
        requete = "INSERT INTO message (id , message , auteur) VALUES (%s, %s, %s)"
        values = (msg,type,auteur)
        self.data.query(requete,values)


    def lecture_message(self):
        requete = "SELECT message FROM message"
        resultat = self.data.query(requete,None)
        return resultat
        
    def lecture_time(self): 
        requete = "SELECT time FROM message"
        resultat = self.data.query(requete,None)
        return resultat
    
    def id_auteur(self,email):
        requete = "SELECT id FROM user where email=%s"
        value = email
        resultat = self.data.query(requete,value)
        return resultat
        
    def lecture_id_auteur(self):   
        requete = "SELECT auteur FROM message "
        resultat = self.data.query(requete,None)
        return resultat
    
    def suppression_message(self):
        requete = "DELETE id from user"
        resultat = self.data.query(requete,None)
        return resultat 
                
if __name__ == "__main__":
    chat = Chat()
    chat.creation_message("hello test",1,1)