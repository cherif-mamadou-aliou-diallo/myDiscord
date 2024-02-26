from customtkinter import *
from PIL import Image,ImageTk
from connectionsql import Connection
import mysql.connector


app = CTk() 
app.geometry("650x550")
app.title = 'MYDISCORD' 

class Page_inscription(Connection):
    def __init__(self):
        self.conn, self.cursor = Connection(host="localhost", user="root", password="0000", database="discord").connection()
        
    
        entry2 = CTkEntry(master=app, placeholder_text="Enter a Username", width=300)
        entry3 = CTkEntry(master=app, placeholder_text="Enter an email or a number phone", width=300)
        entry4 = CTkEntry(master=app, placeholder_text="Create a password", width=300)
        entry2.place(relx=0.5, rely=0.67, anchor="center")
        entry3.place(relx=0.5, rely=0.77, anchor="center")
        entry4.place(relx=0.5, rely=0.87, anchor="center")
        
        btn1 = CTkButton(master=app, text='S\'inscrire', corner_radius=32, command=self.inscription)
        btn1.place(relx = 0.5, rely = 0.95, anchor= 'center')

        
        self.entry2 = entry2
        self.entry3 = entry3
        self.entry4 = entry4
        self.btn1 = btn1
        

    #image discord
    image = Image.open("images/R.png") 
    width, height = 300, 150  # Définissez la largeur et la hauteur souhaitées pour votre image
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    image_label = CTkLabel(master=app, image=photo, text=None)
    image_label.place(relx=0.5, rely=0.05, anchor="center")
    #fin image discord

    #image google
    image_path = "images/google.png"
    button_image = Image.open(image_path)
    # Redimensionner l'image
    new_width = 20  # Nouvelle largeur souhaitée
    new_height = 20  # Nouvelle hauteur souhaitée
    resized_image = button_image.resize((new_width, new_height))
    # Convertir l'image en format Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)
    # Créer un label pour afficher l'image
    image_label = CTkButton(master=app, image=tk_image, text = 'Google', fg_color='white', corner_radius=32, text_color='black')
    image_label.place(relx=0.35, rely=0.53, anchor="center")
 # fin image  google

    #image facebook
    image_path = "images/facebook.png"
    button_image = Image.open(image_path)
    new_width = 20  # Nouvelle largeur souhaitée
    new_height = 20  # Nouvelle hauteur souhaitée
    resized_image = button_image.resize((new_width, new_height))
    # Convertir l'image en format Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)
    # Créer un label pour afficher l'image
    image_label = CTkButton(master=app, image=tk_image, text='Facebook', fg_color='white', text_color='black', corner_radius=32)
    image_label.place(relx=0.65, rely=0.53, anchor = 'center')
 #fin image facebook
    
    


    
  # log in afficher dans l'interface graphique
    label = CTkLabel(master = app, text ='Log In', font=('Arial', 20))
    label.place(relx = 0.5, rely = 0.15, anchor= 'center')
  # s'inscrire afficher dans l'interface graphique
    label1 = CTkLabel(master = app, text ="S'inscrire", font=('Arial', 20))
    label1.place(relx = 0.5, rely = 0.60, anchor= 'center')
    


    def inscription(self):
        query = "INSERT INTO connexion (nom, email, mot_de_pase) VALUES (%s, %s, %s)"
        values = (self.entry2.get(), self.entry3.get(), self.entry4.get())
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("User added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
       
Page_inscription()
app.mainloop()