from loader import bot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config_data.config import headers
from pre_hotels_counting import pre_hotels_counting
import requests


def city_input(message, payload):
    city = message.text
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": city, "locale": "en_US", "langid": "1033", "siteid": "300000001"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    cities_dict = {}
    for elem in data.get('sr'):
        if elem.get('gaiaId', None):
            current_city = {elem.get('regionNames').get('fullName'): elem.get('gaiaId')}
            cities_dict.update(current_city)
        if len(cities_dict) > 4:
            break
    if cities_dict:
        reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for city in cities_dict:
            reply_kb.add(KeyboardButton(city))
        msg = bot.send_message(message.from_user.id, "Выберите город из списка предложенных:",
                               reply_markup=reply_kb)
        bot.register_next_step_handler(msg, pre_hotels_counting, cities_dict, payload)
    else:
        msg = bot.send_message(message.from_user.id, "Похоже что по Вашему запросу ничего не нашлось( "
                                                     "Попробуйте ввести город еще раз.")
        bot.register_next_step_handler(msg, city_input, payload)
