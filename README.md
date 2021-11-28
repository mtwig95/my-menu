# My menu

A web server in Python that exposes an API for a menu in a specific restaurant

## Description

The data that the service provides update daily
The server implements the following API:

(for all GET operations - name and description - string. price - integer)
* GET /drinks - Returns the id, name, description and price of all drinks
* GET /drink/<id> - Returns id, name, description and price of a drink
* GET /pizzas - Returns the id, name, description and price of all pizzas
* GET /pizza/<id> - Returns id, name, description and price of a pizza
* GET /desserts - Returns the id, name, description and price of all desserts
* GET /dessert/<id> - Returns id, name, description and price of a dessert
* POST /order - receives an order and returns its total price.
  Body:
  {
  "drinks": [id_5, id_6],
  "desserts": [id_1, id_2],
  "pizzas": [id_3, id_4]
  }
  Response - {"Total payment is ____"}.

## Getting Started

### Installing

```
pip install Flask
pip install requests
```

### Executing program

* Run each command in a separate terminal
  
```
python timer.py
```
To run the application export the FLASK_APP environment variable:
For Bash
```
export FLASK_APP=menu
flask run
```
For CMD
```
set FLASK_APP=menu
flask run
```
Running on http://127.0.0.1:5000/
```
python test_menu.py
```
