import requests
from flask import Flask, json
from flask import request


app = Flask(__name__)
menu = requests.get(
    'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
menu = json.loads(menu.text)
menu = menu['Data']
categories = menu['categoriesList']


def show_as_json(input):
    return json.dumps(input)


@app.route("/drinks", methods=['GET'])
def get_drinks():
    drinks = get_category('Drinks')
    return json.dumps(format_items(drinks))


@app.route("/drinks/<id>", methods=['GET'])
def get_drink_id(id):
    drinks = format_items(get_category('Drinks'))
    for drink in drinks:
        if drink['dishId'] == int(id):
            return json.dumps(drink)
    return "No such drink"


@app.route("/pizzas", methods=['GET'])
def get_pizzas():
    pizzas = get_category('Pizzas')
    return json.dumps(format_items(pizzas))


@app.route("/pizzas/<id>", methods=['GET'])
def get_pizza_id(id):
    pizzas = format_items(get_category('Pizzas'))
    for pizza in pizzas:
        if pizza['dishId'] == int(id):
            return json.dumps(pizza)
    return "No such pizza"


@app.route("/desserts", methods=['GET'])
def get_desserts():
    desserts = get_category('Desserts')
    return json.dumps(format_items(desserts))


@app.route("/desserts/<id>", methods=['GET'])
def get_dessert_id(id):
    desserts = format_items(get_category('Desserts'))
    for dessert in desserts:
        if dessert['dishId'] == int(id):
            return json.dumps(dessert)
    return "No such dessert"


def get_category(input_category):
    for category in categories:
        if category['categoryName'] == input_category:
            return category['dishList']


def format_items(items):
    formatted_items = []
    for item in items:
        formated_item = {}
        formated_item['dishId'] = item['dishId']
        formated_item['dishName'] = item['dishName']
        formated_item['dishDescription'] = item['dishDescription']
        formated_item['dishPrice'] = item['dishPrice']
        formatted_items.append(formated_item)
    return formatted_items


@app.route("/order/", methods=['GET', 'POST'])
def post_order():
    if request.method == 'POST':
        data = request.form.get(get_drinks()) # a multidict containing POST data
        json.dumps(get_drinks())

    return "ho"
