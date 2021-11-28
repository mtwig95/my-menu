import json

import requests
import schedule

"""
This file load the data from 10bis Arcaffe to json file every day.
"""
def daily_update():
    menu = requests.get(
        'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod'
        '=pickup')
    menu = json.loads(menu.text)
    menu = menu['Data']
    return menu['categoriesList']

def save_menu_to_file():
    menu = daily_update()
    menu_file = open("menu.json", "w")
    json.dump(menu, menu_file)
    menu_file.close()


if __name__ == "__main__":
    while True:
        schedule.every().day.at("09:00").do(save_menu_to_file)
