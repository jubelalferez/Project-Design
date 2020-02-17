import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (item text, id INTEGER PRIMARY KEY, quantity INTEGER, price INTEGER, weight INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts WHERE quantity!='0'")
        rows = self.cur.fetchall()
        return rows

    def insert(self, item, quantity, price, weight):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (item, quantity, price, weight))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, item, quantity, price, weight):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, total = ?, weight = ?, WHERE id = ?",
                         (item, quantity, price, weight, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('jsj.db')
#db.insert("APPLE", "1", "10")
#db.insert("BANANA", "1", "8")
#db.insert("ORANGE", "1", "10")