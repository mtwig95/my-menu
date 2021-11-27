import requests

url = "http://127.0.0.1:5000"


def test_get_drinks_id(id):
    print('\ntesting test_get_drinks_id()')
    response = requests.get(url + f'/drinks/{id}')
    return response


def test_get_desserts_id(id):
    print('\ntesting test_get_desserts_id()')
    response = requests.get(url + f'/desserts/{id}')
    return response


def test_get_pizzas_id(id):
    print('\ntesting test_get_pizzas_id()')
    response = requests.get(url + f'/pizzas/{id}')
    return response


def test_get_drinks():
    print('\ntesting get_drinks()')
    response = requests.get(url + '/drinks')
    return response


def test_get_pizzas():
    print('\ntesting test_get_pizzas()')
    response = requests.get(url + '/pizzas')
    print(response.content)
    return response


def test_get_desserts():
    print('\ntesting test_get_desserts()')
    response = requests.get(url + '/desserts')
    return response


def test_order():
    print('\ntesting order()')
    response = requests.post(url + '/order', json={"drinks": [2055841, 2055844],
                                                   "desserts": [2055835, 2055836],
                                                   "pizzas": [2055830, 2055831]})
    return response


def test_status_code(response):
    sep = '=' * 15
    if run_test_with_example == True:
        print(response.content)
    if response.status_code != 200:
        print(f'{sep}failed, status code:{response.status_code}{sep}')
    else:
        print(f'{sep}test completed successfully{sep}')


run_test_with_example = True

response = test_get_drinks()
test_status_code(response)

response = test_get_desserts()
test_status_code(response)

response = test_get_pizzas()
test_status_code(response)

response = test_get_drinks_id(2055846)
test_status_code(response)

response = test_get_pizzas_id(2055830)
test_status_code(response)

response = test_get_desserts_id(2055835)
test_status_code(response)

response = test_order()
test_status_code(response)
