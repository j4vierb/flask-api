import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    cur = connection.cursor()

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('post 1', 'content 1'))
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('post 2', 'content 2'))

    connection.commit()
    connection.close()

