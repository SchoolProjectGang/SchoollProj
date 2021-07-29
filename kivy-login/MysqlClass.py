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
            print("printed")


Tanay = Mysql('root','t456tt456t','localhost')
Tanay.connect()