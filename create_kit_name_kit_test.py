import sender_stand_request
# Надежда Васильева, 11-я когорта — Финальный проект. Инженер по тестированию плюс
# Функция для проверки запроса на получения заказа по треку заказа

def test_get_order_track():
    track = sender_stand_request.get_order_track()

    assert track.status_code == 200