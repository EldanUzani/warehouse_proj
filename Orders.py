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
        order_valid = Storage_Management.update(order)
        if(order_valid.valid):
            orders.insert(order.order)
            Orders_Info.new_order(order.order_info)
            return 'Order saved'
        return order_valid.lacking

    def update_order (order_id, updated_order):
        current_order = Order_Info.get_order_info(order_id)
        Storage_Management.order_removed(current_order)
        update_valid = Storage_Management.update(updated_order)
        
        if(update_valid.valid):
            orders.update(updated_order.order, Order.order_id == order_id) 
            Orders_Info.update_order(order_id, updated_order.order_info)
            return 'Updated'

        Storage_Management.update(current_order)
        return update_valid.lacking

    def remove_order (order_id):
        orders.delete(Order.order_id == order_id)
        Orders_Info.delete_order(order_id)
        Storage_Management.order_removed(Order_Info.get_order(order_id))
        return 'Order Removed'

    def get_order_by_date (first_date, second_date = ''):
        if(second_date):
            orders = orders.search(Order.order_shipping_date >= first_date 
                                and Order.order_shipping_date < second_date)
        else:
            orders = order.search(Order.order_shipping_date == first_date)
        
        for order in orders:
            order.order_info = Orders_Info.get_order_info(order.order_id)
        
        return orders


    def get_order_by_customer_name(name):
        orders = orders.search(Order.customer_name == name)
        for order in orders:
            order.order_info = Orders_Info.get_order_info(order.order_id)
        return orders
