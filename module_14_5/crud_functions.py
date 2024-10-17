import sqlite3
from random import randint

def initiate_db():
    connection_telegram_db = sqlite3.connect('not_telegram__4.db')
    cursor = connection_telegram_db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
    (ID INTEGER PRIMARY KEY,
     title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY,
     username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')

    connection_telegram_db.commit()
    connection_telegram_db.close()

def get_all_products():
    connection_telegram_db = sqlite3.connect('not_telegram__4.db')
    cursor = connection_telegram_db.cursor()
    cursor.execute('SELECT * FROM Products')
    product_list = cursor.fetchall()
    connection_telegram_db.close()
    return product_list


def add_user(username, email, age):
    connection_telegram_db = sqlite3.connect('not_telegram__4.db')
    cursor = connection_telegram_db.cursor()
    if is_included(username) is False:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES ( ?, ?, ?, ?)",
                       (username, email, age, 1000))
    connection_telegram_db.commit()
    connection_telegram_db.close()



def is_included(username):
    connection_telegram_db = sqlite3.connect('not_telegram__4.db')
    cursor = connection_telegram_db.cursor()
    list_users = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    fetch_ = list_users.fetchone()
    connection_telegram_db.close()
    if fetch_ is None:
        return False
    else:
        return True


# def show_users():
#     connection_telegram_db = sqlite3.connect('not_telegram__4.db')
#     cursor = connection_telegram_db.cursor()
#     users_list = cursor.execute('SELECT * FROM Users')
#     message = ''
#     for _ in users_list:
#         message += f'{_[0]}, {_[1]}, {_[2]}, {_[3]} ''\n'
#     connection_telegram_db.close()
#     return message



# connection_telegram_db = sqlite3.connect('not_telegram__4.db')
# cursor = connection_telegram_db.cursor()
# # cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES ( ?, ?, ? )", ('newuser', 'ex@gmail.com', '28' ))
# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age, balance ) VALUES ( ?, ?, ?, ? )", (f'newuser{i}', f'ex{i}@gmail.com', f'{randint(20,50)}', 1000 ))
#
# connection_telegram_db.commit()
# connection_telegram_db.close()





# for i in range(0, 4):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES ( ?, ?, ?)',
#                    (f'Продукт {i + 1}', f'Описание {i + 1}', (i+1) * 100))
# connection_telegram_db.commit()
# connection_telegram_db.close()



