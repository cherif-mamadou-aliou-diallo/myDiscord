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
        
        
        # Fond de l'interface graphique
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
        image_label.place(relx=0.5, rely=0.07, anchor="center")
        
        entry2 = CTkEntry(master=app, placeholder_text="Enter a Username", width=300, corner_radius=32)
        entry3 = CTkEntry(master=app, placeholder_text="Enter an email or a number phone", width=300,corner_radius=32)
        entry4 = CTkEntry(master=app, placeholder_text="Create a password", width=300,corner_radius=32)
        entry2.place(relx=0.5, rely=0.3, anchor="center")
        entry3.place(relx=0.5, rely=0.4, anchor="center")
        entry4.place(relx=0.5, rely=0.5, anchor="center")
        
        btn1 = CTkButton(master=app, text='S\'inscrire', corner_radius=32, command=self.inscription)
        btn1.place(relx = 0.5, rely = 0.6, anchor= 'center')

        
        self.entry2 = entry2
        self.entry3 = entry3
        self.entry4 = entry4
        self.btn1 = btn1
        

    #image discord
    
    

 
  # s'inscrire afficher dans l'interface graphique
    label1 = CTkLabel(master = app, text ="S'inscrire", font=('Arial', 20))
    label1.place(relx = 0.5, rely = 0.2, anchor= 'center')
    
    
    def inscription(self):
        query = "INSERT INTO connexion (nom, email, mot_de_pase) VALUES (%s, %s, %s)"
        values = (self.entry2.get(), self.entry3.get(), self.entry4.get())
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("User added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
       

if __name__ == '__main__':    
    inscription = Page_inscription()
    app.mainloop()