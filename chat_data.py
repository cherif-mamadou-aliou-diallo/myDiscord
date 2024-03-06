import mysql.connector
from mysql.connector import Error
from database import Data

# La classe Chat interagit avec une base de données de la classe Data :
class Chat(Data):
    def __init__(self):
        #  Cela appelle le constructeur de la classe parente Data.
        Data.__init__(self)
        # En appelant self.connected(), la classe Chat établit une connexion à la base de données lors de son initialisation.
        self.connected()

#  La méthode insère un nouveau message dans la table message de la base de données avec le contenu du message (msg),
#   l'ID de l'auteur (auteur) et le type de message (type).
#  Les valeurs par défaut pour l'auteur et le type sont respectivement 1.
    def creation_message(self, msg, auteur=1,type=1):
        requete = "INSERT INTO message (message ,auteur,type_message) VALUES (%s, %s, %s)"
        values = (msg,auteur,type) #  value : les valeurs à insérer.
        self.query(requete,values,modif=True) #modif = True indique qu'il ne faut pas s'attendre à un résultat en retour.

# La méthode lecture_message sélectionne tous les messages de la table message de la base de données et les retourne.
    def lecture_message(self):
        requete = "SELECT message FROM message"
        resultat = self.query(requete) # La méthode query est utilisée pour exécuter des requêtes SQL sur la base de données.
        return resultat
    
    #Cette méthode sélectionne toutes les dates/heure des messages de la table message de la base de données et les retourne.
    def lecture_time(self): 
        requete = "SELECT time FROM message"
        resultat = self.query(requete)
        return resultat
    # la méthode id_auteur sélectionne l'ID de l'utilisateur correspondant à l'e-mail donné de la table user de la base de données et le retourne.
    def id_auteur(self,email):
        requete = "SELECT id FROM user where email=%s"
        value = email
        resultat = self.query(requete,value)
        return resultat
    
    # La méthode lecture_id_auteur sélectionne tous les IDs d'auteurs des messages de la table message de la base de données et les retourne.
    
    def lecture_id_auteur(self):   
        requete = "SELECT auteur FROM message"
        resultat = self.query(requete,None) #la requête SQL (requete) et None comme valeur pour les paramètres (value).
        # Cela peut signifier qu'il n'y a pas de paramètres nécessaires pour cette requête spécifique.
        return resultat
    
    # Cette méthode supprime un message de la table message en fonction de l'ID donné.
    def suppression_message(self, id):
        requete = "DELETE FROM message WHERE id = %s"
        value = (id ,)
        self.query(requete, value, modif = True)
        print("Message supprimé avec succès!") 
        
        # Appelle différentes méthodes de la classe Chat        
if __name__ == "__main__":
    chat = Chat() # Création de l'instance de la classe Chat
    # chat.creation_message("Le test à démarré correctement !")
    print(chat.lecture_message())
    # print(chat.id_auteur())
    # print(chat.lecture_id_auteur())
    # chat.suppression_message(2)
    
    # -------------------Version Inter_graphique----------------------------
    
