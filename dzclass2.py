import sqlite3

conn = sqlite3.connect('DATA3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_2 INTEGER) ''')

class Database:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def database1(self, a):
        if a is True:
            cursor.execute('''INSERT INTO tab_1(col_2) VALUES ("3")''')

    def database2(self, a, b):
        if type(b) == int and a is True:
            cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')

    def database3(self, a, b, c):
        if type(c) == int and a is True and b is True:
            cursor.execute('''UPDATE tab_1 SET col_2 = 77 WHERE id = 3''')

    def printdb(self):
        cursor.execute('''SELECT * FROM tab_1''')

x = Database(1, 2, 3)
print(x)


