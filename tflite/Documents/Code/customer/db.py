import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, item text, quantity INTEGER, price INTEGER, weight INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT id, item, quantity, price, weight FROM parts WHERE quantity > 0")
        rows = self.cur.fetchall()
        return rows
        
    def addcustomer(self,orange, apple, banana):
        self.cur.execute("INSERT INTO orders VALUES (NULL, ?, ?, ?)",
                         (orange, apple, banana))
        self.conn.commit()

    def remove(self, id1):
        self.cur.execute("UPDATE parts SET quantity = 0, price = 0, weight = 0 WHERE id = ?", (id1,))
        self.conn.commit()
        if id1 == 1:
            self.cur.execute("UPDATE orders SET orange = 0 WHERE orderid = (SELECT orderid FROM orders ORDER BY orderid DESC LIMIT 1)")
            self.conn.commit()
        elif id1 == 2:
            self.cur.execute("UPDATE orders SET apple = 0 WHERE orderid = (SELECT orderid FROM orders ORDER BY orderid DESC LIMIT 1)")
            self.conn.commit()
        elif id1 == 3:
            self.cur.execute("UPDATE orders SET banana = 0 WHERE orderid = (SELECT orderid FROM orders ORDER BY orderid DESC LIMIT 1)")
            self.conn.commit()

    def reset_all(self):
        self.cur.execute("UPDATE parts SET quantity = 0, price = 0, weight = 0")
        self.conn.commit()

    def updateorange(self):
        self.cur.execute("UPDATE orders SET orange = orange + 1 WHERE orderid =(SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)")
        self.cur.execute("UPDATE parts SET quantity = (SELECT orange from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        price = 10*(SELECT orange from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        weight = 135*(SELECT orange from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1))\
        WHERE id = 1")
        self.conn.commit()

    def updateapple(self):
        self.cur.execute("UPDATE orders SET apple = apple + 1 WHERE orderid =(SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)")
        self.cur.execute("UPDATE parts SET quantity = (SELECT apple from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        price = 10*(SELECT apple from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        weight = 145*(SELECT apple from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1))\
        WHERE id = 2")         
        self.conn.commit()

    def updatebanana(self):
        self.cur.execute("UPDATE orders SET banana = banana + 1 WHERE orderid =(SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)")
        self.cur.execute("UPDATE parts SET quantity = (SELECT banana from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        price = 8*(SELECT banana from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1)),\
        weight = 120*(SELECT banana from orders WHERE orderid = (SELECT orderid from orders ORDER BY orderid DESC LIMIT 1))\
        WHERE id = 3")       
        self.conn.commit()

    def display_price(self):
        self.cur.execute("SELECT SUM(price) FROM parts")
        tprice= self.cur.fetchall()
        return tprice 

    def display_weight(self):
        self.cur.execute("SELECT SUM(weight) FROM parts")
        tweight= self.cur.fetchall()
        return tweight 

    def fetch_orange(self):
        self.cur.execute("SELECT id, item, quantity, price, weight FROM parts where id = 1 AND quantity > 0")
        forange= self.cur.fetchall()
        return forange

    def fetch_apple(self):
        self.cur.execute("SELECT id, item, quantity, price, weight FROM parts where id = 2 AND quantity > 0")
        fapple= self.cur.fetchall()
        return fapple

    def fetch_banana(self):
        self.cur.execute("SELECT id, item, quantity, price, weight FROM parts where id = 3 AND quantity > 0")
        fbanana= self.cur.fetchall()
        return fbanana

    def fetch_orderid(self):
        self.cur.execute("SELECT orderid FROM orders ORDER BY orderid DESC LIMIT 1")
        forderid = self.cur.fetchall()
        return forderid

    def upinvent(self):
        self.cur.execute("UPDATE inventory SET quantity = quantity - (SELECT orange FROM orders ORDER BY orderid DESC LIMIT 1) WHERE id = 1")
        self.conn.commit()
        self.cur.execute("UPDATE inventory SET quantity = quantity - (SELECT apple FROM orders ORDER BY orderid DESC LIMIT 1) WHERE id = 2")
        self.conn.commit()
        self.cur.execute("UPDATE inventory SET quantity = quantity - (SELECT banana FROM orders ORDER BY orderid DESC LIMIT 1) WHERE id = 3")
        self.conn.commit()

    def resetbox1(self):
        self.cur.execute("UPDATE orders SET orange = 0, apple = 0, banana = 0 WHERE orderid = (SELECT orderid FROM orders ORDER BY orderid DESC LIMIT 1)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database(r'C:\Users\Jubel\Desktop\db\jsj.db')