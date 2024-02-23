# import socket
# # import tkinter as tk
# import threading

# class Serveur:
#     def __init__(self, ip, port):
#         self.IP = ip
#         self.PORT = port
#         self.serveur = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#         self.clients = []
#         self.pseudos = []

#     def diffuser(self, message):
#         for client in self.clients :
#             client.send(bytes(message , "utf-8"))

#     def gestion_connexion(self):
#         while True : 
#             client, adresse = self.serveur.accept()
#             print(f"Connexion réussie avec {str(adresse)}")
#             pseudo = client.recv(1024).decode("utf-8")

#             self.clients.append(client)
#             self.pseudos.append(pseudo)

#             print(f"{pseudo} vient de rejoindre le chat")
#             client.send(bytes("Bienvenue dans le chat \n", "utf-8"))
#             self.diffuser(f"{pseudo} a rejoint le chat")

#             thread_client = threading.Thread(target=self.gestion_client, args=(client, pseudo))
#             thread_client.start()

#     def gestion_client(self, client, pseudo):
#         while True :
#             try :
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

#             except : 
#                 index = self.clients.index(client)

#                 self.clients.remove(client)
#                 client.close()

#                 pseudo = self.pseudos[index]
#                 self.pseudos.remove(pseudo)

#                 self.diffuser(f"{pseudo} a quitté le chat")
#                 break

#     def demarrer_serveur(self):
#         self.serveur.bind((self.IP , self.PORT))
#         self.serveur.listen(10)
#         print("Le serveur de chat est en marche.")
#         self.gestion_connexion()

# # Utilisation de la classe ServeurChat
# if __name__ == "__main__":
#     IP = "127.0.0.1"
#     PORT = 55555
#     serveur = Serveur(IP, PORT)
#     serveur.demarrer_serveur()
# --------------------------------------------------------------------------------------------------
# import tkinter as tk
# import socket
# import threading

# class Serveur:
#     def __init__(self, ip, port):
#         self.IP = ip
#         self.PORT = port
#         self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
#             client.send(bytes("Bienvenue dans le chat \n", "utf-8"))
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

# def demarrer_serveur():
#     global serveur
#     IP = "127.0.0.1"
#     PORT = 55555
#     serveur = Serveur(IP, PORT)
#     serveur.demarrer_serveur()

# def afficher_interface():
#     global root
#     root = tk.Tk()
#     root.title("Serveur de Chat")
#     root.geometry("900x600")  # Largeur : 400 pixels, Hauteur : 300 pixels

    

#     start_button = tk.Button(root, text="Démarrer Serveur", command=demarrer_serveur)
#     start_button.pack()

#     root.mainloop()

# thread_interface = threading.Thread(target=afficher_interface)
# thread_interface.start()

import tkinter as tk
from tkinter import PhotoImage
import socket
import threading
import pygame

class Serveur:
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.pseudos = []

    # Autres méthodes de la classe Serveur ici...

def demarrer_serveur():
    global serveur
    IP = "127.0.0.1"
    PORT = 55555
    serveur = Serveur(IP, PORT)
    serveur.demarrer_serveur()

def afficher_interface():
    global root
    root = tk.Tk()
    root.title("Serveur de Chat")

    # Charger l'image de fond
    background_image = PhotoImage(file="background_image.png")

    # Créer un canevas pour afficher l'image de fond
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Démarrer la musique
    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)  # -1 pour répéter en boucle

    start_button = tk.Button(root, text="Démarrer Serveur", command=demarrer_serveur)
    start_button.pack()

    root.mainloop()

thread_interface = threading.Thread(target=afficher_interface)
thread_interface.start()
