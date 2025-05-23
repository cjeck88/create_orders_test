# Тест на проверку получения данных о заказе по треку заказа в Яндекс.Самокат с помощью API Яндекс.Самокат.
- Выполнить запрос на создание заказа.
- Сохранить номер трека заказа.
- Выполнить запрос на получения заказа по треку заказа.
- Проверить, что код ответа равен 200.

# Структура проекта.
- yandex_api_samokat_test:
    - configuration.py # Пути и базовый URL
    - create_order_test.py # Набор тестов
    - sender_stand_request.py: POST-запрос на создание заказа, GET-запросы на получение номера заказа и на получение заказа по номеру
    - data.py # Тестовые данные (user_orders)
    - README.md # Документация проекта
    - .gitignore # Исключения
    
# Запуск тестов.
- Запуск теста выполняется командой pytest
- pytest test_order_api.py -v

# Типы тестирования.
- Позитивное автотестирование 

# Что проверяет тест
- после запроса на получение заказа по треку заказа приходит код ответа 200

# Пример тест-кейсов.
-   №	Описание	                                ОР: Код ответа — 200
    1	данные пользователя для создания заказа:         В ответе есть ключ "order" — значит, заказ нашёлся и получен успешно
user_orders = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}	

# Рекомендации.
- Использовать актуальный URL Яндекс.Самокат
- Для запуска тестов должны быть установлены пакеты pytest, requests