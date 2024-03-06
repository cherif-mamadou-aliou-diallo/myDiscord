from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
from PIL import Image, ImageTk
from tkinter import messagebox
from chat import Chat  # Assuming your chat class is defined in chat.py

class ChatGUI(CTk):
    def __init__(self):
        super().__init__()
        self.title("Discord")
        self.geometry("500x400")

        # Background image
        background_image = Image.open("images/c.jpeg")
        width, height = 900, 750
        background_image = background_image.resize((width, height))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = CTkLabel(self.master, image=background_photo, text='')
        background_label.image = background_photo  # Keep a reference to the image to prevent garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.chat = Chat()  # Create an instance of your Chat class
        
        # Create widgets
        self.label = CTkLabel(self, text="Enter message:")
        self.entry = CTkEntry(self,corner_radius=32, width=300)
        self.entry.place(relx=0.4, rely=0.9, anchor="center")
        self.button_send = CTkButton(self, text="Send Message", corner_radius=32,command=self.send_message, width=100)
        self.button_send.place(relx=0.85, rely=0.9, anchor="center")
        self.button_display = CTkButton(self, text="Display Messages", corner_radius=32, command=self.display_messages,width=100)
        self.button_display.place(relx=0.9, rely=0.1, anchor="center")
        
        # Layout
        
    
    def send_message(self):
        message = self.entry.get()
        if message:
            self.chat.creation_message(message, "type_here", "author_here")
            messagebox.showinfo("Success", "Message sent successfully!")
            self.entry.delete(0, CTk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a message.")
    
    def display_messages(self):
        messages = self.chat.lecture_messages()
        messagebox.showinfo("Messages", "\n".join(messages))

if __name__ == "__main__":
    app = ChatGUI()
    app.mainloop()
