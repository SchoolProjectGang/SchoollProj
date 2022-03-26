import mysql.connector as con
import json


class Mysql:
    def __init__(self):
        with open('./cache/creds.json', 'r') as f:
            password = json.load(f)
        self.m = con.connect(
            host='localhost',
            username='yash',
            password=password['password'],
            database=password['database']
        )
        self.user_id = 0
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

    # check if login credentials are correct or not
    def check_creds(self, username, password):
        self.cursor.execute(
            f"select uid, userpassword from users where username='{username}'")
        user_data = self.cursor.fetchall()
        if user_data:
            self.user_id = user_data[0][0]
            if password == user_data[0][1]:
                return username
            else:
                return False
        else:
            return False

    def check_first_letter(self, username, password):
        if username == '' or password == '':
            return False
        if username[0] == ' ' or password[0] == ' ':
            return False
        return True

    def get_game_list(self):
        self.cursor.execute("select * from Products")
        return self.cursor.fetchall()

    def add_game(self, name, username):
        # list of products
        self.cursor.execute(f"select * from Products where name='{name}'")
        creds = self.cursor.fetchall()
        print(creds)

        # list of users
        self.cursor.execute(f"select * from users where username='{username}'")
        info = self.cursor.fetchall()
        print(info)
        self.cursor.execute(
            f"update users set total_amount_spent={creds[0][2] + (info[0][3] if info[0][3] is not None else 0)}, games_owned='{str(creds[0][0]) + ' ' + (str(info[0][4]) if info[0][4] is not None else '')}' where username='{username}'")
        self.m.commit()
