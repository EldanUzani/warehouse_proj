from tinydb import TinyDB, Query, where
from tinydb.operations import delete , increment, decrement, add, subtract, set
from datetime import timedelta , datetime, date , time

db = TinyDB('db.json')
orders = db.table('orders')
Order = query()

some_date = datetime(2022, 5 , 15)

order1 = {
    'order_id' : 1
    'date_ordered': str(some_date.date()),
    'time_ordered': str(some_date.time()),
    'order_shipping_date': '2022-10-15',
    'order_retriving_date': '2022-10-22',
    'customer_name': 'Moshe haviv',
    'order_location': 'Haifa',}

order1_info = {
    'order_id' : 1
    'legs': 15,
    'profiles': 20,
    'refrigeretaros':3,
    }

order = {'order':order1, 'order_info': order1_info}

class Orders:
    def new_order (order):
        order_valid = Storage_Management.check_if_available(order.order_info)
        if(order_valid.valid):
            orders.insert(order.order)
            Orders_Info.new_order(order.order_info)
            Storage_Management.update(order.order_info)
            return 'Order saved'
        return order_valid.lacking

    def update_order (order_id, order):
        update_valid = Storage_Management.check_if_available(order.order_info)
        if(update_valid.valid):
            orders.update(order.order, Order.order_id == order_id) 
            Order_Info.update_order(order_id, order.order_info)
            Storage_Management.update(Orders_Info.get_order(order_id))
            return 'Updated'
        return update_valid.lacking

    def check_for_existing_order (order_name):
        return True

    def remove_order (order_id):
        orders.delete(Order.order_id == order_id)
        Order_Info.delete_order(order_id)
        Storage_Management.update(Order_Info.get_order(order_id))
        return True