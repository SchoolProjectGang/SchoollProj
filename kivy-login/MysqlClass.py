import mysql.connector as con


class Mysql:
    def __init__(self):
        self.m = con.connect(
            host='localhost',
            username='root',
            password='t456tt456t',
            database='project'
        )
        if self.m.is_connected():
            self.cursor = self.m.cursor()

    def make_database(self, dbname):
        self.cursor.execute(f"create database {dbname}")
        self.m.commit()
        return

    def drop_database(self, dbname):
        self.cursor.execute(f"drop database {dbname}")
        self.m.commit()
        return

    def add_userdata(self, name1, pass1):
        self.cursor.execute(
            f"insert into users(username,userpassword) values('{name1}','{pass1}')")
        self.m.commit()
        # print(f"insert into users(username,userpassword) values('{name1}','{pass1}')")
        return
