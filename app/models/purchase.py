from flask import current_app as app


class Purchase:
    def __init__(self, orderid, totalprice, totalQt, time_purchased, isFulfill):
        self.orderid = orderid
        self.totalprice = totalprice
        self.totalQt = totalQt
        self.time_purchased = time_purchased
        self.isFulfill = isFulfill

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, uid, pid, time_purchased
FROM Purchases
WHERE id = :id
''',
                              id=id)
        return Purchase(*(rows[0])) if rows else None

    @staticmethod
    def get_all_by_uid_since(uid, since):
        rows = app.db.execute('''
SELECT id, SUM(finalprice*quantity),SUM(quantity), MAX(time_purchased) as time, EVERY(fulfillstate)
FROM Purchases
WHERE uid = :uid AND time_purchased >= :since
GROUP BY id
ORDER BY time DESC
''',
            uid=uid, since=since)
        return [Purchase(*row) for row in rows]
  
class OrderDetail:
    def __init__(self, pid, productname, sid, sellerlastname, sellerfirstname,  quantity, final_unitprice, fulfilled):
        self.pid = pid
        self.productname = productname
        self.sid = sid
        self.sellerlastname = sellerlastname
        self.sellerfirstname = sellerfirstname
        self.quantity = quantity
        self.final_unitprice = final_unitprice
        self.fulfilled = fulfilled

    @staticmethod
    def getOrderDetail(orderid):
        uidRow = app.db.execute('''
SELECT MAX(uid) FROM purchases
WHERE id=:id GROUP BY id
''',     id=orderid)

        orderRows = app.db.execute('''
SELECT purchases.pid, products.name, purchases.sid, users.lastname, users.firstname, purchases.quantity, purchases.finalprice, purchases.fulfillstate
FROM purchases, products, users
WHERE purchases.id=:orderid
AND products.id=purchases.pid
AND users.id=purchases.sid
''',        orderid=orderid)
        return uidRow[0][0], [OrderDetail(*row) for row in orderRows]

class FilteredItem:
    def __init__(self,orderid, time_purchased, pid, productname, sid, sellerlastname, sellerfirstname, quantity, final_unitprice, fulfilled):
        self.orderid = orderid
        self.time_purchased = time_purchased
        self.pid = pid
        self.productname = productname
        self.sid = sid
        self.sellerlastname = sellerlastname
        self.sellerfirstname = sellerfirstname
        self.quantity = quantity
        self.final_unitprice = final_unitprice
        self.fulfilled = fulfilled
    
    @staticmethod
    def getFilteredItem(productNameKeyword, sellerLastNameKeyword, sellerFirstNameKeyword, uid):
        rows = app.db.execute(f'''
SELECT purchases.id, purchases.time_purchased, purchases.pid, products.name, purchases.sid, users.lastname, users.firstname, purchases.quantity, purchases.finalprice, purchases.fulfillstate
FROM purchases, products, users
WHERE purchases.uid=:uid
AND products.id=purchases.pid
AND users.id=purchases.sid
AND products.name LIKE '{"%"+productNameKeyword+"%"}'
AND users.lastname LIKE '{"%"+sellerLastNameKeyword+"%"}'
AND users.firstname LIKE '{"%"+sellerFirstNameKeyword+"%"}'
ORDER BY purchases.time_purchased DESC
''', uid=uid)
        return  [FilteredItem(*row) for row in rows]
