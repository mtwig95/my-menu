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
        s.enter(60 * 60, 10, save_menu_to_file, (s,))
        s.run()

minutes = 60

# # schedule.every(1).minutes.do(self.local, script_path)
# # schedule.every().day.at("11:08").do(save_menu_to_file)
# # schedule.every().day.at("11:08").do(check_timer())
# # schedule.every().minute.at(":23").do(save_menu_to_file)
#
# @repeat(every(10).seconds)
# def job():
#     print("I am a scheduled job")
#
#
#
# schedule.every(3).seconds.do(save_menu_to_file)
# schedule.every(3).minutes.do(save_menu_to_file)
# schedule.every(3).hours.do(save_menu_to_file)
# schedule.every(3).days.do(save_menu_to_file)
# schedule.every(3).weeks.do(save_menu_to_file)
