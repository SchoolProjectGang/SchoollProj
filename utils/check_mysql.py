import mysql.connector as con


def check(password: str, database: str):
    try:
        con.connect(
            host='localhost',
            username='root',
            password=password,
            database=database
        )
        return True
    except:
        return False
