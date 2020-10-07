import sqlite3
import json

db = sqlite3.connect('users.db')
sql = db.cursor()


def add_user_to_db(message):
    msg = json.loads(str(message))
    id = msg["from"]["id"]
    first_name = msg["from"]["first_name"]
    username = msg["from"]["username"] #without @

    #Checking аvailability of user
    query_find_clone = "SELECT COUNT(1) FROM users where id = " + str(id)
    sql.execute(query_find_clone)
    number_of_clones = sql.fetchall()
    if number_of_clones[0][0] == 0:
        query_add_user = f"INSERT INTO users VALUES (?, ?, ?)"
        sql.execute(query_add_user, (id, first_name, username))
        db.commit()
        #print("Добавлен")
    else:
        return
        #print("Хуй тебе, я таких как ты " + str(number_of_clones[0][0]) + " нашел")

def take_all_users():
    sql.execute("""
        SELECT * FROM users
    """)
    all_users = sql.fetchall()
    print(all_users)

def delete_user():
    sql.execute("""
        DELETE FROM users
        WHERE username = 'Кашин'
    """)
    db.commit()
    take_all_users()
