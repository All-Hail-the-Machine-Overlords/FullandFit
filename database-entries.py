import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS restaurants(name TEXT, menu TEXT, id REAL)')

def data_entry():
    c.execute("INSERT INTO restaurants VALUES ('Panda Express', 'Menu', 01)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()