import mysql.connector
from PIL import Image,ImageTk
from mysql.connector import Error
from connectionsql import Connection
from interface import Interface_chat


class Chat(Connection):


    def __init__(self):
        self.conn, self.cursor = Connection(host="localhost", user="root", password="0000", database="discord").connection()
        
        

    # Cette fonction construit une requête SQL d'insertion pour ajouter un nouveau message dans la table message avec les valeurs spécifiées.
    def creation_message(self,type,auteur):
        query = "INSERT INTO message (id , message , auteur) VALUES (%s, %s, %s)"
        values = (self.entry.get(),type,auteur)
        try:
            self.cursor.execute(query, values) # Exécute la requête SQL spécifiée dans la variable query en utilisant les valeurs passées dans la variable values.
            self.conn.commit() # Valide toutes les modifications qui ont été faites depuis le dernier commit dans la base de données.
            print("Utilisateur ajouté avec succès !")
        except Error as err:
            print(f"Erreur: {err}")
            
    # Cette fonction est utilisée pour lire tous les messages enregistrés dans la table message.
    # Elle construit une requête SQL de sélection (SELECT * FROM message), puis l'exécute à l'aide du curseur (self.cursor).
    
    def lecture_messages(self):
        query = "SELECT * FROM message"
        self.cursor.execute(query)
        messages = self.cursor.fetchall()
        for message in messages: # chaque élément de la liste messages sera imprimé à la console.
            print(message)
            
    
    
    #ANCHOR - NB : (try-except) est utilisée pour gérer les erreurs éventuelles qui pourraient survenir
    # lors de l'exécution de la requête SQL et de la validation des modifications dans la base de données.
    
    # Cette fonction est utilisée pour mettre à jour un message existant dans la table message.
    # Elle prend en paramètres l'identifiant (id) du message à mettre à jour.
    
    def mise_a_jour_message(self, id, msg, type,auteur):
        query = "UPDATE message SET message = %s, type = %s, auteur = %s WHERE id = %s"
        values = (msg, type,auteur, id)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Le message à été mis à jour avec succès !")
        except Error as err:
            print(f"Erreur: {err}")
            
    # Cette fonction est utilisée pour supprimer un message existant dans la table message.
    # Elle prend en paramètre l'identifiant (id) du message à supprimer.
    
    def supprimer_message(self, id):
        query = "DELETE FROM message WHERE id = %s"
        values = (id,)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Message supprimé avec succès !")
        except Error as err:
            print(f"Erreur: {err}")
            
    # Cette fonction est utilisée pour fermer la connexion à la base de données. 
    def femreture(self):
        # La condition vérifie si la connexion à la base de données est active avant de la fermer. 
        if self.conn.is_connected(): # est une méthode qui vérifie si la connexion à la base de données est toujours active.
            self.cursor.close() # est appelé pour fermer le curseur utilisé pour exécuter des requêtes SQL.
            self.conn.close() # est appelé pour fermer la connexion à la base de données.
                
if __name__ == "__main__":
    chat = Chat()
    chat.creation_message("hello test",1,1)
