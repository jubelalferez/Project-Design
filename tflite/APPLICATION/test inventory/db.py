import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM inventory")
        rows = self.cur.fetchall()
        return rows     

    def __del__(self):
        self.conn.close()

db = Database(r'C:\Users\Jubel\Desktop\db\jsj.db')