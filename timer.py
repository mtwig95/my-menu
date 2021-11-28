"""
This file load the data from 10bis Arcaffe to json file every day.
"""
import json
import sched
import time

import requests


def daily_update():
    menu = requests.get(
        'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod'
        '=pickup')
    menu = json.loads(menu.text)
    menu = menu['Data']
    return menu['categoriesList']


def save_menu_to_file(sc):
    print(f'MAYTAL TIME {time.asctime()}')

    menu = daily_update()
    menu_file = open("menu.json", "w")
    json.dump(menu, menu_file)
    menu_file.close()
    s.enter(10, 1, save_menu_to_file, (sc,))


if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)

    while True:
        s.enter(60 * 60, 24, save_menu_to_file, (s,))
        s.run()
