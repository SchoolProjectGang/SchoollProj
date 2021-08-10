import mysql.connector as con


class Mysql:
    def __init__(self):
        self.m = con.connect(
            host='localhost',
            username='root',
            password='t456tt456t',
            database='project'
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
            return password == user_data[0][1]
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
