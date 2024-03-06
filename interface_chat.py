from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
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

        # Create a frame to display messages
        self.frame = CTkFrame(self, width=400, height=200, bg_color='white')
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.message_index = 0  # Index to keep track of message placement
        
    def send_message(self):
        message = self.entry.get()
        if message:
            self.chat.creation_message(message, "type_here", "author_here")
            print("test")
            message_label = CTkLabel(self.frame, text=f"You: {message}", anchor="w")
            message_label.grid(row=self.message_index, column=0, sticky="w")
            self.message_index += 1
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
