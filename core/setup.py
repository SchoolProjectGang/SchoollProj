import json


def is_empty():
    with open('./cache/creds.json', 'r+') as f:
        creds = (json.load(f))
        if creds['password'] == "" or creds['database'] == "":
            # creds are empty, run setup
            return True
        else:
            return False


def modify(password: str, database: str):
    with open('./cache/creds.json', 'r+') as f:
        json.dump({'password': password, 'database': database}, f, indent=4)
