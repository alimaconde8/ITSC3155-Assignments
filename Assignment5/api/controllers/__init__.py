# api/controllers/__init__.py
from .orders import create_order, read_all_orders, read_one_order, update_order, delete_order
from .sandwiches import create_sandwich, read_all_sandwiches, read_one_sandwich, update_sandwich, delete_sandwich
# Similarly import functions from other controller files as needed

def resources():
    return None

def recipes():
    return None

def order_details():
    return None
