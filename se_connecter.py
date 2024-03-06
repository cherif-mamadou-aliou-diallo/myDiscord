import os
import webbrowser
from customtkinter import *
from PIL import Image, ImageTk
from connectionsql import Connection

app = CTk() 
app.geometry("650x550")
app.title = 'MYDISCORD' 

class connection(Connection):
    def __init__(self) -> None:
        self.conn, self.cursor = Connection(host="localhost", user="root", password="0000", database="discord").connection()
        
        background_image = Image.open("images/c.jpeg")
        width, height = 980, 880
        background_image = background_image.resize((width, height))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = CTkLabel(master=app, image=background_photo, text='')
        background_label.image = background_photo  # Garder une référence à l'image pour éviter la collecte des déchets
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        image = Image.open("images/image.png") 
        width, height = 270, 80  # Définissez la largeur et la hauteur souhaitées pour votre image
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        image_label = CTkLabel(master=app, image=photo, text=None)
        image_label.place(relx=0.5, rely=0.06, anchor="center")

        image = Image.open("images/google.png")
        image = image.resize((30, 30))  # Redimensionner l'image si nécessaire
        google_logo = ImageTk.PhotoImage(image)
        
        image = Image.open("images/facebook.png")
        image = image.resize((30, 30))  # Redimensionner l'image si nécessaire
        facebook_logo = ImageTk.PhotoImage(image)
        
        # Créer le bouton avec l'image de Google
        btn1 = CTkButton(master=app, corner_radius=32, fg_color='white', text_color='black', image=google_logo, compound="left", text='google', command=self.open_google)
        btn1.place(relx=0.35, rely=0.45, anchor='center')

        btn2 = CTkButton(master=app, corner_radius=32, fg_color='white', text_color='black', image=facebook_logo, compound="left", text='facebook', command=self.open_facebook)
        btn2.place(relx=0.65, rely=0.45, anchor='center')

        entry = CTkEntry(master=app, placeholder_text="email adresse ", width=300, corner_radius=32)
        entry1 = CTkEntry(master=app, placeholder_text="password", width=300, corner_radius= 32)

        entry.place(relx=0.5, rely=0.25, anchor="center")
        entry1.place(relx=0.5, rely=0.35, anchor="center")

        btn = CTkButton(master=app, text='se connecter', corner_radius=32, command=self.se_connecter)
        btn.place(relx=0.5, rely=0.55, anchor='center')
        
        btn_signup = CTkButton(app, text="Sign Up", corner_radius=32, fg_color='white', text_color='black', command=self.inscription)
        btn_signup.place(relx=0.395, rely=0.6)

        self.entry1 = entry1
        self.entry = entry
        self.btn = btn
        self.btn_signup = btn_signup
        self.btn1 = btn1

        self.label = CTkLabel(master=app, text='Log In', font=('Arial', 20))
        self.label.place(relx=0.5, rely=0.15, anchor='center')

    def open_google(self):
        url = "https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1%26nlr%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-486272840%3A1709647108022243&theme=mn"
        webbrowser.open_new(url)
    
    def open_facebook(self):
        url = "https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F%3Flocale%3Dfr_FR"
        webbrowser.open_new(url)

    

    def inscription(self):
        os.system('python inscription.py')
    
    
    
    
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

connecter = connection()
app.mainloop()
