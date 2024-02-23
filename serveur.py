# import socket
# import tkinter as tk
# import threading
# import pyaudio

# class Serveur:
#     def __init__(self, ip, port):
#         self.IP = ip
#         self.PORT = port
#         self.serveur = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#         self.clients = []
#         self.pseudos = []

#     def diffuser(self, message):
#         for client in self.clients:
#             client.send(bytes(message, "utf-8"))

#     def gestion_connexion(self):
#         while True:
#             client, adresse = self.serveur.accept()
#             print(f"Connexion réussie avec {str(adresse)}")
#             pseudo = client.recv(1024).decode("utf-8")

#             self.clients.append(client)
#             self.pseudos.append(pseudo)

#             print(f"{pseudo} vient de rejoindre le chat")
#             # client.send(bytes("Bienvenue dans le chat \n", "utf-8"))
            
#             self.diffuser(f"{pseudo} a rejoint le chat")

#             thread_client = threading.Thread(target=self.gestion_client, args=(client, pseudo))
#             thread_client.start()

#     def gestion_client(self, client, pseudo):
#         while True:
#             try:
#                 message = client.recv(1024).decode("utf-8")

#                 if message == "exit":
#                     index = self.clients.index(client)

#                     self.clients.remove(client)
#                     client.close()

#                     pseudo = self.pseudos[index]
#                     self.pseudos.remove(pseudo)

#                     self.diffuser(f"{pseudo} a quitté le chat")
#                     break

#                 else:
#                     self.diffuser(f"{pseudo} : {message}")

#             except:
#                 index = self.clients.index(client)

#                 self.clients.remove(client)
#                 client.close()

#                 pseudo = self.pseudos[index]
#                 self.pseudos.remove(pseudo)

#                 self.diffuser(f"{pseudo} a quitté le chat")
#                 break

#     def demarrer_serveur(self):
#         self.serveur.bind((self.IP, self.PORT))
#         self.serveur.listen(10)
#         print("Le serveur de chat est en marche.")
#         self.gestion_connexion()

# class ServeurApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Serveur de Chat")
#         self.geometry("400x200")

#         self.serveur = Serveur("10.10.87.153", 60555)

#         self.start_button = tk.Button(self, text="Démarrer Serveur", command=self.demarrer_serveur)
#         self.start_button.pack()

#     def demarrer_serveur(self):
#         self.start_button.configure(state=tk.DISABLED)
#         threading.Thread(target=self.serveur.demarrer_serveur).start()
#         ChatWindow(self)

# class ChatWindow(tk.Toplevel):
#     def __init__(self, master):
#         super().__init__(master)
#         self.title("Chat")
#         self.geometry("400x300")

#         self.chat_text = tk.Text(self)
#         self.chat_text.pack(fill=tk.BOTH, expand=True)

#         self.message_entry = tk.Entry(self)
#         self.message_entry.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#         self.send_button = tk.Button(self, text="Envoyer Message", command=self.envoyer_message)
#         self.send_button.pack(side=tk.BOTTOM)  # Placement en bas de la fenêtre

#         self.audio_button = tk.Button(self, text="Chat Vocal", command=self.envoyer_audio)
#         self.audio_button.pack(side=tk.BOTTOM)  # Placement en bas de la fenêtre

#     def envoyer_message(self):
#         message = self.message_entry.get()
#         if message:
#             self.master.serveur.diffuser(f"{self.master.serveur.pseudos[0]} : {message}")
#             self.message_entry.delete(0, tk.END)

#     def envoyer_audio(self):
#         CHUNK = 1024
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 1
#         RATE = 44100

#         audio = pyaudio.PyAudio()

#         stream = audio.open(format=FORMAT, channels=CHANNELS,
#                             rate=RATE, input=True,
#                             frames_per_buffer=CHUNK)

#         print("Enregistrement audio en cours...")

#         frames = []

#         for _ in range(0, int(RATE / CHUNK * 5)):  # Enregistre pendant 5 secondes
#             data = stream.read(CHUNK)
#             frames.append(data)

#         print("Enregistrement audio terminé.")

#         stream.stop_stream()
#         stream.close()
#         audio.terminate()

#         self.master.serveur.diffuser(f"{self.master.serveur.pseudos[0]} a envoyé un message vocal.")

# if __name__ == "__main__":
#     app = ServeurApp()
#     app.mainloop()


# -----------------------------------------------------------------------------------------------------------------------------------------------------
 
import tkinter as tk
import socket
import select
import threading

HEADER_LENGTH = 10
IP = "localhost"
PORT = 5566

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

root = tk.Tk()
root.title("Historique de Chat")

messages_frame = tk.Frame(root)
scrollbar = tk.Scrollbar(messages_frame)  
msg_list = tk.Listbox(messages_frame, height=15, width=50, bg="black", fg =""  , yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
messages_frame.pack()

entry_field = tk.Entry(root, width=50)
entry_field.pack()

clients = {}  # Variable clients initialisée

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

def send_message():
    message = entry_field.get()
    entry_field.delete(0, tk.END)
    for client_socket in clients:
        client_socket.send(message.encode('utf-8'))

sockets_list = [server_socket]  # Variable sockets_list initialisée

def update_chat():
    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                user = receive_message(client_socket)
                if user is False:
                    continue
                sockets_list.append(client_socket)
                clients[client_socket] = user
                msg_list.insert(tk.END, 'Nouvelle connexion acceptée de {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
            else:
                message = receive_message(notified_socket)
                if message is False:
                    msg_list.insert(tk.END, 'Connexion fermée à partir de: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]
                msg_list.insert(tk.END, f'Message reçu de {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]

def start_thread():
    thread = threading.Thread(target=update_chat)
    thread.daemon = True
    thread.start()

def on_closing():
    server_socket.close()  # Fermer proprement le socket serveur
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)  # Gérer la fermeture de la fenêtre
send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack()

start_thread()
root.mainloop()





