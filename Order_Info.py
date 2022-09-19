from tinydb import TinyDB, Query, where
from tinydb.operations import delete , increment, decrement, add, subtract, set

db = TinyDB('db.json')
orders_info = db.table('orders_info')
Order_Info = Query()

class Orders_Info:

    def new_order(order_info):
        orders_info.insert(order_info)

    def update_order(order_id, updated_order):
        order_info.update(updated_order, Order_info.order_id == order_id)

    def remove_order(order_id):
        order_info.delete(Order_Info.order_id == order_id)
