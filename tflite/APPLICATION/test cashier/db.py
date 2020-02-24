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

    def getordero(self,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT id, item, (SELECT orange FROM orders WHERE orderid = ?),\
        ((SELECT orange FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 1)),\
        ((SELECT orange FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 1))\
         FROM parts WHERE id = 1",(orderid1,orderid2,orderid3,))
        fetch_order = self.cur.fetchall()
        return fetch_order
    
    def getordera(self,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT id, item, (SELECT apple FROM orders WHERE orderid = ?),\
        ((SELECT apple FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 2)),\
        ((SELECT apple FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 2))\
         FROM parts WHERE id = 2",(orderid1,orderid2,orderid3,))
        fetch_order = self.cur.fetchall()
        return fetch_order

    def getorderb(self,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT id, item, (SELECT banana FROM orders WHERE orderid = ?),\
        ((SELECT banana FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 3)),\
        ((SELECT banana FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 3))\
         FROM parts WHERE id = 3",(orderid1,orderid2,orderid3,))
        fetch_order = self.cur.fetchall()
        return fetch_order

    def getordertp(self,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT SUM(((SELECT orange FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 1))\
        +((SELECT apple FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 2))\
        +((SELECT banana FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 3)))"\
        ,(orderid1,orderid2,orderid3,))
        fetch_order = self.cur.fetchall()
        return fetch_order

    def getordertw(self,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT SUM(((SELECT orange FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 1))\
        +((SELECT apple FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 2))\
        +((SELECT banana FROM orders WHERE orderid = ?)*(SELECT weight FROM inventory WHERE id = 3)))"\
        ,(orderid1,orderid2,orderid3,))
        fetch_order = self.cur.fetchall()
        return fetch_order

    def __del__(self):
        self.conn.close()


db = Database(r'C:\Users\Jubel\Desktop\db\jsj.db')  


#db.insert("APPLE", "1", "10")
#db.insert("BANANA", "1", "8")
#db.insert("ORANGE", "1", "10")