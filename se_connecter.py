from customtkinter import *
from PIL import Image,ImageTk
from connectionsql import Connection



app = CTk() 
app.geometry("650x550")
app.title = 'MYDISCORD' 

class connection(Connection):
    def __init__(self) -> None:
        self.conn, self.cursor = Connection(host="localhost", user="root", password="0000", database="discord").connection()

        entry = CTkEntry(master = app, placeholder_text="email adresse ", width=300,)
        entry1 = CTkEntry(master = app, placeholder_text="password", width=300)

        entry.place (relx=0.5, rely=0.25, anchor ="center")
        entry1.place (relx=0.5, rely=0.35, anchor ="center")

        btn = CTkButton(master = app, text ='se connecter', corner_radius = 32, command=self.se_connecter)
        btn.place(relx = 0.5, rely = 0.45, anchor= 'center')

        self.entry1 = entry1
        self.entry = entry
        self.btn = btn
        

    label = CTkLabel(master = app, text ='Log In', font=('Arial', 20))
    label.place(relx = 0.5, rely = 0.15, anchor= 'center')

        

    def se_connecter(self):
        email = self.entry.get()
        password = self.entry1.get()

    # Exécuter la requête SQL pour sélectionner les enregistrements correspondant à l'email et au mot de passe saisis
        query = "SELECT * FROM connexion WHERE email = %s AND mot_de_pase = %s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()

    # Vérifier si un enregistrement est trouvé
        if result:
            print("Vous êtes connecté.")
        else:
            print("Email ou mot de passe incorrect.")
connection()

app.mainloop()
