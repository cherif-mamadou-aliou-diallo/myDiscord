import mysql.connector
from PIL import Image,ImageTk
from mysql.connector import Error
from database import Data
from customtkinter import *

app = CTk() 
app.geometry("600x500")
app.title = 'MYDISCORD' 

class Chat(Data):
    def __init__(self):
        self.conn, self.cursor = Data(host="localhost", user="root", password="0000", database="discord").connected()
        
        entry = CTkEntry(master=app, placeholder_text="tap something", width=300, corner_radius=32)
        entry.place(relx=0.47, rely=0.9, anchor="center")
        btn = CTkButton(master=app, text='Send', corner_radius=32)
        btn.place(relx = 0.85, rely = 0.9, anchor= 'center')

        self.entry = entry

    image = Image.open("images/c.jpeg") 
    width, height = 900 ,750
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)

    

    app.configure(background="white")  # Assurez-vous que le fond est blanc pour éviter les distorsions de l'image
    background_label = CTkLabel(app, image=photo, text='')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image = Image.open("images/discord (1).png") 
    width, height = 70, 50  # Définissez la largeur et la hauteur souhaitées pour votre image
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    image_label = CTkLabel(master=app, image=photo, text=None)
    image_label.place(relx=0.1, rely=0.09, anchor="center")


    # Cette fonction construit une requête SQL d'insertion pour ajouter un nouveau message dans la table message avec les valeurs spécifiées.
    def creation_message(self, msg, type,auteur):
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
app.mainloop()