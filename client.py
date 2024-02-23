# import tkinter as tk
# from tkinter import scrolledtext
# import socket
# import threading

# class Client:
#     def __init__(self, ip, port):
#         self.IP = ip
#         self.PORT = port
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.pseudo = None

#     def connecter(self):
#         self.client.connect((self.IP, self.PORT))
#         self.pseudo = input("Entrez votre pseudo: ")
#         self.client.send(bytes(self.pseudo, "utf-8"))

#     def envoyer_message(self, event=None):
#         message = self.message_entry.get()
#         self.client.send(bytes(message, "utf-8"))
#         self.message_entry.delete(0, tk.END)

#     def reception(self):
#         while True:
#             try:
#                 message = self.client.recv(1024).decode("utf-8")
#                 self.chat_history.insert(tk.END, message + '\n')
#                 self.chat_history.see(tk.END)
#             except:
#                 break

# class ClientApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Client Chat")

#         self.IP = "10.10.87.153"
#         self.PORT = 60555

#         self.client = Client(self.IP, self.PORT)

#         self.message_entry = tk.Entry(self)
#         self.message_entry.pack(side=tk.BOTTOM, fill=tk.X)
#         self.message_entry.bind("<Return>", self.client.envoyer_message)

#         self.chat_history = scrolledtext.ScrolledText(self, wrap=tk.WORD)
#         self.chat_history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

#         self.client.connecter()
#         threading.Thread(target=self.client.reception).start()

# if __name__ == "__main__":
#     app = ClientApp()
#     app.mainloop()

# --------------------------------
import tkinter as tk
import socket
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "localhost"
PORT = 5566

mon_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = mon_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

root = tk.Tk()
root.title(f"Chat Client - {mon_username}")

messages_frame = tk.Frame(root)
scrollbar = tk.Scrollbar(messages_frame)  
msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tk.Entry(root, width=50)
entry_field.pack()

def send_message(event=None):
    message = entry_field.get()
    entry_field.delete(0, tk.END)
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

def receive_message():
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connexion fermée par le serveur')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            msg_list.insert(tk.END, f'{username} > {message}')
            msg_list.yview(tk.END)
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        root.after(100, receive_message)
    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()

root.protocol("WM_DELETE_WINDOW", root.quit)
entry_field.bind("<Return>", send_message)
send_button = tk.Button(root, text="Envoyer", command=send_message, bd=3, relief=tk.RAISED, font=("Helvetica", 12))
send_button.pack()

root.after(100, receive_message)
root.mainloop()

# ---------------

# import tkinter as tk
# import socket
# import select
# import errno
# import sys
# import threading

# HEADER_LENGTH = 10
# IP = "localhost"
# PORT = 5566

# class Client:
#     def __init__(self, username):
#         self.username = username
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client_socket.connect((IP, PORT))
#         self.client_socket.setblocking(False)

#         self.send_username()

#     def send_username(self):
#         username = self.username.encode('utf-8')
#         username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
#         self.client_socket.send(username_header + username)

#     def send_message(self, message):
#         if message:
#             message = message.encode('utf-8')
#             message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
#             self.client_socket.send(message_header + message)

#     def receive_messages(self):
#         while True:
#             try:
#                 username_header = self.client_socket.recv(HEADER_LENGTH)
#                 if not len(username_header):
#                     print('Connection closed by the server')
#                     sys.exit()
#                 username_length = int(username_header.decode('utf-8').strip())
#                 username = self.client_socket.recv(username_length).decode('utf-8')
#                 message_header = self.client_socket.recv(HEADER_LENGTH)
#                 message_length = int(message_header.decode('utf-8').strip())
#                 message = self.client_socket.recv(message_length).decode('utf-8')
#                 yield f'{username} > {message}'
#             except IOError as e:
#                 if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                     print('Reading error:', str(e))
#                     sys.exit()
#                 continue
#             except Exception as e:
#                 print('Reading error:', str(e))
#                 sys.exit()

# class ChatUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chat Client")

#         self.messages_frame = tk.Frame(self.root)
#         self.scrollbar = tk.Scrollbar(self.messages_frame)  
#         self.msg_list = tk.Listbox(self.messages_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
#         self.msg_list.pack()
#         self.messages_frame.pack()

#         self.entry_field = tk.Entry(self.root, width=50)
#         self.entry_field.pack()

#         self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bd=3, relief=tk.RAISED, font=("Helvetica", 12))
#         self.send_button.pack()

#     def send_message(self):
#         message = self.entry_field.get()
#         self.entry_field.delete(0, tk.END)
#         client.send_message(message)

#     def update_messages(self, message):
#         if message:
#             self.msg_list.insert(tk.END, message)
#             self.msg_list.yview(tk.END)

# if __name__ == "__main__":
#     mon_username = input("Username: ")

#     root = tk.Tk()
#     chat_ui = ChatUI(root)

#     client = Client(mon_username)

#     def receive_messages():
#         for message in client.receive_messages():
#             chat_ui.update_messages(message)

#     receive_thread = threading.Thread(target=receive_messages)
#     receive_thread.start()

#     root.mainloop()





