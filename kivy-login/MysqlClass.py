import mysql.connector as con

class Mysql:
    def __init__(self, username, password, host) -> None:
        self.username = username
        self.password = password
        self.host = host


    def connect(self):
        self.m = con.connect(
            host = self.host,
            username = self.username,
            password = self.password
        )
        if self.m.is_connected():
            self.cursor = self.m.cursor()
            print("connected")
            # self.drop_database("NEWDB")
    
    def make_database(self,dbname):
        self.cursor.execute(f"create database {dbname}")
        self.m.commit()
        return 

    def drop_database(self,dbname):
        self.cursor.execute(f"drop database {dbname}")
        self.m.commit()
        return

userinput_u = input("enter your mysql username please thanks!")
userinput_p = input("enter your mysql password please thanks!") 
local_instance = Mysql(userinput_u, userinput_p, 'localhost')
local_instance.connect()
