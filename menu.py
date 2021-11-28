from flask import Flask, json, request

app = Flask(__name__)

"""
this function return the data from the file
"""
def get_menu():
    menu_file = open("menu.json", "r")
    output = json.loads(menu_file.read())
    menu_file.close()
    return output


@app.route("/")
def index():
    return """
    <h1>Planck's Tech Assignment</h1>
    <h2>Web server in Python that exposes an API for a menu in a specific restaurant</h2>
    """


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
        body = request.json #to get the body
        total_payment = 0
        for category in body.keys():
            category_items = get_category(category.title())
            for id in body.get(category, "No item"):
                item_price = get_price_by_id(category_items, id)
                total_payment += item_price
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
    for category in menu_categories:
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


"""
the var getting all the categories from the menu
"""
menu_categories = get_menu()
