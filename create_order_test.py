import sender_stand_request
import requests
import data
import configuration

# Анастасия Найдина, Mars08a
# 1-я когорта — Финальный проект. Инженер по тестированию плюс
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

def get_order_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMDER +"?t=" + str(track_number))

def positive_assert():
    order_response = post_new_order(data.order_body)
    #print(order_response.status_code)
    #print(order_response.json())
    track_number_order = (order_response.json()["track"])
    #print(track_number_order)
    number_response = get_order_number(track_number_order)
    #print(number_response.json())
    assert number_response.status_code == 200

# Тест. Успешное получение заказа по его номеру
def test_create_order_number_get_success_response():
    positive_assert()
