import requests
from configuration import URL_SERVICE, CREATE_ORDERS_PATH, USERS_KITS_PATH
from data import user_orders, headers

# Функция для создания заказа
def create_order():
    response = requests.post(URL_SERVICE + CREATE_ORDERS_PATH,
                             json=user_orders,
                             headers=headers)
    return response

# Функция для получения информации о заказе по треку
def get_order_by_track(track):
    response = requests.get(URL_SERVICE + USERS_KITS_PATH, params={"t": track})
    return response