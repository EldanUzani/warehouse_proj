from tinydb import TinyDB, Query, where
from tinydb.operations import delete, increment, decrement, add, subtract, set
from datetime import timedelta, datetime, date, time

db = TinyDB('db.json')
storage_management = db.table('storage_management')
Storage_Management_Tool = Query()

class Storage_Management():

    def update(order):
        storage_matching = storage_management.search(Storage_Management_Tool.date >= order.order_shipping_date
                                                     and Storage_Management_Tool.date < order.order_retriving_date)
        storage_matching.sort(key=lambda storage_obj: storage_obj.date)

        for temporary_storage_by_datetime in storage_matching:
            Storage_Management.data_calculator(temporary_storage_by_datetime, order.order_info)
            storage_management.update(temporary_storage_by_datetime, Storage_Management_Tool.date == temporary_storage_by_datetime.date)

        new_storage_to_insert = Storage_Management.return_latest_date_before_current_storage_obj(order.order_shipping_date)
        Storage_Management.data_calculator(new_storage_to_insert, order.order_info)

        new_storage_to_insert.date = order.order_shipping_date
        storage_management.insert(new_storage_to_insert)

        storage_matching[-1].date = order.order_retriving_date
        Storage_Management.data_calculator(storage_matching[-1], order_info, -1)
        storage_management.insert(storage_matching[-1])

    def check_if_available(order):
        available_analisys = []

        storage_matching = storage_management.search(Storage_Management_Tool.date >= order.order_shipping_date
                                                     and Storage_Management_Tool.date < order.order_retriving_date)

        for temporary_storage_by_datetime in storage_matching:
            results = Storage_Management.data_calculator(temporary_storage_by_datetime, order.order_info)
            available_analisys_date_time = [temporary_storage_by_datetime.date]
            for item, amount in results:
                if amount < 0:
                    available_analisys_date_time.append((item, amount))

            available_analisys.append(available_analisys_date_time)

    def order_removed(order):
        pass

    def get_order_by_date(order):
        pass

    def data_calculator(storage_obj, order_info, act=1):
        """return result tuple list [('item_name', amount), ('item_name', amount)]"""
        result_array = []

        for item in order_info:
            if item == 'order_id':
                continue
            storage_obj.item -= act*order_info.item
            result_array.append((item, storage_obj[item]))

        return result_array

    def return_latest_date_before_current_storage_obj(current_date):
        before_current_date_objs = storage_management.search(Storage_Management_Tool.date < current_date)
        before_current_date_objs.sort(key=lambda storage_obj: storage_obj.date)
        return before_current_date_objs[0]






