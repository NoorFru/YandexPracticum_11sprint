import configuration
import requests
import data


# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response=post_new_order(data.order_body);
print(response.status_code)
print(response.json())

# Запрос на получения заказа по треку заказа
def get_order_track():
    track_body = str(post_new_order(data.order_body).json()['track'])
    return requests.get(configuration.URL_SERVICE + configuration.FIND_OUT_ORDER + track_body)
response=get_order_track()
print(response.status_code)
print(response.json())