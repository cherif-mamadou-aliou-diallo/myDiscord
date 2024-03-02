import mysql.connector


class Data :
    def __init__(self, host, user, password, database):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connected(self):
        conn = mysql.connector.connect(
            host=self.host,
            user= self.user,
            password = self.password,
            database = self.database
        )
        cursor = conn.cursor()
        return conn, cursor
    
    def close_data(self):
        pass
    