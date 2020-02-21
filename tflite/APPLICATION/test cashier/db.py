import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT id, item, quantity, price, weight FROM parts WHERE quantity > 0")
        rows = self.cur.fetchall()
        return rows    

    def display_price(self):
        self.cur.execute("SELECT SUM(price) FROM parts")
        tprice= self.cur.fetchall()
        return tprice 

    def display_weight(self):
        self.cur.execute("SELECT SUM(weight) FROM parts")
        tweight= self.cur.fetchall()
        return tweight

    def reset_all(self):
        self.cur.execute("UPDATE parts SET quantity = 0, price = 0, weight = 0")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database(r'C:\Users\Owen\Desktop\db\jsj.db')  


#db.insert("APPLE", "1", "10")
#db.insert("BANANA", "1", "8")
#db.insert("ORANGE", "1", "10")