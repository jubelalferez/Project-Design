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

    def getordero(self,orderid1,orderid2,orderid3,orderid4):
        self.cur.execute("SELECT id, item, (SELECT orange FROM orders WHERE orderid = ? AND orange > 0),\
        ((SELECT orange FROM orders WHERE orderid = ? AND orange > 0)*(SELECT price FROM inventory WHERE id = 1)),\
        ((SELECT orange FROM orders WHERE orderid = ? AND orange > 0)*(SELECT weight FROM inventory WHERE id = 1))\
         FROM parts WHERE id = 1 AND (SELECT orange FROM orders where orderid = ? AND orange > 0)",(orderid1,orderid2,orderid3,orderid4,))
        fetch_order = self.cur.fetchall()
        return fetch_order
    
    def getordera(self,orderid1,orderid2,orderid3,orderid4):
        self.cur.execute("SELECT id, item, (SELECT apple FROM orders WHERE orderid = ? AND apple > 0),\
        ((SELECT apple FROM orders WHERE orderid = ? AND apple > 0)*(SELECT price FROM inventory WHERE id = 2)),\
        ((SELECT apple FROM orders WHERE orderid = ? AND apple > 0)*(SELECT weight FROM inventory WHERE id = 2))\
         FROM parts WHERE id = 2 AND (SELECT apple FROM orders where orderid = ? AND apple > 0)",(orderid1,orderid2,orderid3,orderid4,))
        fetch_order = self.cur.fetchall()
        return fetch_order

    def getorderb(self,orderid1,orderid2,orderid3,orderid4):
        self.cur.execute("SELECT id, item, (SELECT banana FROM orders WHERE orderid = ? AND banana > 0),\
        ((SELECT banana FROM orders WHERE orderid = ? AND banana > 0)*(SELECT price FROM inventory WHERE id = 3)),\
        ((SELECT banana FROM orders WHERE orderid = ? AND banana > 0)*(SELECT weight FROM inventory WHERE id = 3))\
         FROM parts WHERE id = 3 AND (SELECT banana FROM orders where orderid = ? AND banana > 0)",(orderid1,orderid2,orderid3,orderid4,))
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

    def getchange(self,cashenter,orderid1,orderid2,orderid3):
        self.cur.execute("SELECT ? - (SELECT SUM(((SELECT orange FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 1))\
        +((SELECT apple FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 2))\
        +((SELECT banana FROM orders WHERE orderid = ?)*(SELECT price FROM inventory WHERE id = 3))))"\
        ,(cashenter,orderid1,orderid2,orderid3,))
        fetch_change = self.cur.fetchall()
        return fetch_change

    def __del__(self):
        self.conn.close()


db = Database(r'\\raspberrypi\share\jsj.db')  


#db.insert("APPLE", "1", "10")
#db.insert("BANANA", "1", "8")
#db.insert("ORANGE", "1", "10")