"# menu" 
$env:FLASK_APP="menu"
flask run


test:
import requests
response = requests.request('POST','http://127.0.0.1:5000/order', json={'drinks':2055841,1:2055831})
"drinks": [id_5, id_6],
"desserts": [id_1, id_2],
"pizzas": [id_3, id_4]

response = requests.request('POST','http://127.0.0.1:5000/order', json={'drinks':2055841,'desserts':2055831,'pizzas':2055830,2055831})
pizza =
2055830 50
,2055831 55
2055833, "dishName": "Goat cheese and arugula", "dishPrice": 55}]
drink - 2055841 - spritr - 12, 2055844 water 10
desserts':2055831
@app.route("/order", methods=['POST'])
def post_order():
if request.method == 'POST':
print(request)
body = request.json
print(body)
total_payment = 0
for id in body.values():
total_payment += get_price_by_id(id)
print(total_payment)
return "Total psyment is {}".format(total_payment)

