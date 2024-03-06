from customtkinter import *
from PIL import Image, ImageTk


class Interface_chat:

    def __init__(self, master):
        self.master = master
        self.master.geometry("600x500")
        self.master.title('MYDISCORD')
   
        # Background image
        background_image = Image.open("images/c.jpeg")
        width, height = 900, 750
        background_image = background_image.resize((width, height))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = CTkLabel(self.master, image=background_photo, text='')
        background_label.image = background_photo  # Keep a reference to the image to prevent garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Entry field
        entry = CTkEntry(master=self.master, placeholder_text="Tap something", width=300, corner_radius=32)
        entry.place(relx=0.47, rely=0.9, anchor="center")
        # Send button
        btn = CTkButton(master=self.master, text='Send', corner_radius=32)
        btn.place(relx=0.85, rely=0.9, anchor='center')

        self.entry = entry
        self.btn = btn

        # Discord logo
        discord_image = Image.open("images/image.png")
        width, height = 140, 60
        discord_image = discord_image.resize((width, height))
        discord_photo = ImageTk.PhotoImage(discord_image)
        discord_label = CTkLabel(master=self.master, image=discord_photo, text=None)
        discord_label.image = discord_photo  # Keep a reference to the image to prevent garbage collection
        discord_label.place(relx=0.12, rely=0.08, anchor="center")

        

if __name__ == "__main__":
    app = CTk()
    Interface_chat(app)
    app.mainloop()
