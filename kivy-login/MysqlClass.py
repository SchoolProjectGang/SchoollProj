import mysql.connector as con

class Mysql:
    def __init__(self) -> None:
        self.username = 'root'
        self.password = 't456tt456t'
        self.host = 'localhost'
    
    # def main(self):
    #     pass    # manages the class calls and everything


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
    def make_table(self, tbname, f1, f2, f3, f4, f5, f6):
        self.cursor.execute(f"create table {tbname}({f1},{f2}, {f3}, {f4}, {f5}, {f6}) ")
        self.m.commit()
        return
    def drop_table(self, tbname):
        self.cursor.execute(f"drop table {tbname}")
        self.m.commit()
        return
# userinput_u = input("enter your mysql username please thanks!")
# userinput_p = input("enter your mysql password please thanks!") 
# local_instance = Mysql(userinput_u, userinput_p, 'localhost')
# local_instance.connect()
