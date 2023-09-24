import configuration
import requests
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=order_body)  # тут тело

order_response = post_new_order(data.order_body);
print(order_response.status_code)
print(order_response.json())
track_number_order = (order_response.json()["track"])




