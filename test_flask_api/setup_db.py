# Script to setup SQLite database "users.db" with users.json data

import sqlite3
import json

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER,
        location TEXT
    )
''')

with open('users.json') as usersfile:
    users = json.load(usersfile)
    for user in users:
        cursor.execute('INSERT INTO users (id, name, email, age, location) VALUES (?, ?, ?, ?, ?)', 
                       (user['id'], user['name'], user['email'], user['age'], user['location']))

conn.commit()
conn.close()
