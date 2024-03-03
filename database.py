import mysql.connector as mc
from dotenv import load_dotenv
import os
load_dotenv()

class Data :
    def __init__(self):
        self.__host = os.getenv("host"),
        self.__user = os.getenv("user"),
        self.__password = os.getenv("password"),
        self.__database = os.getenv("database")
        # pass
    def connected(self):
        conn = mc.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__database
        )
        cursor = conn.cursor()
        return conn, cursor
    
    def close_data(self):
        pass
    