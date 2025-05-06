import requests
import pytest
from configuration import URL_SERVICE, CREATE_ORDERS_PATH, USERS_KITS_PATH
from data import user_orders, headers
# Евгений Твердохлебов, 29-я когорта - Финальный проект. Инженер по тестированию расширенный.
def test_create_and_get_order():
    # Создание заказа
    create_response = requests.post(URL_SERVICE + CREATE_ORDERS_PATH,
                                     json=user_orders,
                                     headers=headers)
    assert create_response.status_code == 201, "Не удалось создать заказ"
    track = create_response.json().get("track")
    assert track is not None, "Track не вернулся в ответе"

    # Получение заказа по треку
    get_response = requests.get(URL_SERVICE + USERS_KITS_PATH, params={"t": track})
    assert get_response.status_code == 200, "Не удалось получить заказ по треку"
    assert "order" in get_response.json(), "Ответ не содержит заказ"



