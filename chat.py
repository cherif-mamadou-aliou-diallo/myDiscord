from database import Data

class Chat(Data):
    def __init__(self):
        self.conn, self.cursor = Data(host="localhost", user="root", password="0000", database="discord").connected()
        
    
    def creer_message(self, msg, type=1, auteur):
        