# Евгений Твердохлебов, 29-я когорта - Финальный проект. Инженер по тестированию расширенный.
import pytest
from sender_stand_request import create_order, get_order_by_track

def test_create_and_get_order():
    # Создание заказа
    create_response = create_order()
    assert create_response.status_code == 201, "Не удалось создать заказ"
    
    # Извлекаем трек из ответа
    track = create_response.json().get("track")
    assert track is not None, "Track не вернулся в ответе"
    
    # Получение заказа по треку
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, "Не удалось получить заказ по треку"
    assert "order" in get_response.json(), "Ответ не содержит заказ"




