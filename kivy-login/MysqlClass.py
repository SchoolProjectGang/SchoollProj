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

userinput_u = input('enter your mysql username please thanks!")
userinput_p = input('enter your mysql password please thanks!") 
userinput_h = input('enter your mysql hostname please thanks!")
Tanay = Mysql(userinput_u, userinput_p, userinput_h)
Tanay.connect()
