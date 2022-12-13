import sqlite3
import random

conn = sqlite3.connect('DATA2.db')
cursor = conn.cursor()


b = random.randint(1, 30)
c = random.randint(1, 30)
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_2 INTEGER, col_3 INTEGER) ''')
cursor.execute('''INSERT INTO tab_1(col_2, col_3) VALUES ( ?, ?)''', (b, c))

conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()

for i in k:
    print(i)