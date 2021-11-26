import requests
from flask import Flask, json, request

app = Flask(__name__)


def daily_update():
    menu = requests.get(
        'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
    menu = json.loads(menu.text)
    menu = menu['Data']
    return menu['categoriesList']


@app.route("/drinks", methods=['GET'])
def get_drinks():
    return show_as_json(get_category('Drinks'))


@app.route("/pizzas", methods=['GET'])
def get_pizzas():
    return show_as_json(get_category('Pizzas'))


@app.route("/desserts", methods=['GET'])
def get_desserts():
    return show_as_json(get_category('Desserts'))


@app.route("/drinks/<id>", methods=['GET'])
def get_drink_id(id):
    return get_item('Drinks', id)


@app.route("/pizzas/<id>", methods=['GET'])
def get_pizza_id(id):
    return get_item('Pizzas', id)


@app.route("/desserts/<id>", methods=['GET'])
def get_dessert_id(id):
    return get_item('Desserts', id)


@app.route("/order", methods=['POST'])
def post_order():
    if request.method == 'POST':
        body = request.json
        total_payment = 0
        for category in body.keys():
            category_items = get_category(category.title())
            for id in body.get(category, "No item"):
                item_price = get_price_by_id(category_items, id)
                total_payment += item_price
        print("*"*20)
        return "Total payment is {}".format(total_payment)


def show_as_json(input):
    return json.dumps(input)


def get_item(category, id):
    category = get_category(category)
    for item in category:
        if item['dishId'] == int(id):
            return show_as_json(item)
    return "<h1>No such item</h1>"


def get_category(input_category):
    for category in categories:
        if category['categoryName'] == input_category:
            return format_items(category['dishList'])


def format_items(items):
    formatted_items = []
    for item in items:
        formatted_item = {'dishId': item['dishId'], 'dishName': item['dishName'],
                          'dishDescription': item['dishDescription'], 'dishPrice': item['dishPrice']}
        formatted_items.append(formatted_item)
    return formatted_items


def get_price_by_id(category, id):
    for item in category:
        if item['dishId'] == int(id):
            return item['dishPrice']


categories = daily_update()
# body = {'drinks': [2055841, 2055844], 'desserts': [2055835, 2055836], 'pizzas': [2055830, 2055831]}
# print(body)
# print(post_order(body))
# categories = daily_update()
# item = get_item('Drinks', 2055841)
# id = 2055841
# # print(get_price_by_id(id))
# x = 1
