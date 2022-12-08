from loader import bot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config_data.config import headers
from functions.hotels_counting import hotels_counting
import requests


def city_input(message, payload, flag):
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
        bot.register_next_step_handler(msg, pre_hotels_counting, cities_dict, payload, flag)
    else:
        msg = bot.send_message(message.from_user.id, "Похоже что по Вашему запросу ничего не нашлось( "
                                                     "Попробуйте ввести город еще раз.")
        bot.register_next_step_handler(msg, city_input, payload, flag)


def pre_hotels_counting(message, cities_dict, payload, flag):
    selected_city = message.text
    if selected_city not in cities_dict.keys():
        msg = bot.send_message(message.from_user.id, "Город не распознан. Введите его заново:")
        bot.register_next_step_handler(msg, city_input, payload)
    else:
        selected_city_id = cities_dict.get(selected_city)
        payload["destination"]["regionId"] = selected_city_id
        if flag:
            msg = bot.send_message(message.from_user.id, "Необходимо указать диапазон цен для поиска. "
                                                         "Укажите минимальную цену за ночь: ")
            bot.register_next_step_handler(msg, min_price_step, payload)
        else:
            msg = bot.send_message(message.from_user.id, "Отлично, теперь укажите необходимое количество отелей на "
                                                         "вывод (не более 30).", reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, hotels_counting, payload)


def check_price(user_id, price, func_name, payload, compare_num=0):
    if not price.isdigit():
        msg = bot.send_message(user_id,
                               "Цена должна быть указана в числовом формате (например 300). Попробуйте еще раз:")
        bot.register_next_step_handler(msg, func_name, payload, compare_num)
    elif int(price) < compare_num:
        msg = bot.send_message(user_id, f"Текущая цена не можеть быть меньше {compare_num}! Попробуйте еще раз:")
        bot.register_next_step_handler(msg, func_name, payload, compare_num)
    else:
        return int(price)


def min_price_step(message, payload, compare_num=0):
    min_price = message.text
    valid_min_price = check_price(message.from_user.id, min_price, min_price_step, payload)
    if valid_min_price:
        msg = bot.send_message(message.from_user.id, "Теперь укажите максимальную цену за ночь:")
        bot.register_next_step_handler(msg, max_price_step, payload, valid_min_price)


def max_price_step(message, payload, min_price):
    max_price = message.text
    valid_max_price = check_price(message.from_user.id, max_price, max_price_step, payload, compare_num=min_price)
    if valid_max_price:
        payload["price_range"] = [min_price, valid_max_price]
        msg = bot.send_message(message.from_user.id,
                               "Отлично, теперь необходимо указать диапазон расстояния отеля от центра. Укажите "
                               "минимальное расстояние:")
        bot.register_next_step_handler(msg, min_distance_step, payload)


def check_distance(user_id, distance, func_name, payload, compare_distance=0):
    try:
        valid_distance = float(distance)
        if valid_distance <= compare_distance:
            msg = bot.send_message(user_id,
                                   f"Текущее расстояние не может быть меньше {compare_distance}! Попробуйте еще раз:")
            bot.register_next_step_handler(msg, func_name, payload, compare_distance)
        else:
            return valid_distance
    except ValueError:
        msg = bot.send_message(user_id, "Расстояние должно быть указано в числовом формате (например 3). Попробуйте "
                                        "еще раз:")
        bot.register_next_step_handler(msg, func_name, payload, compare_distance)


def min_distance_step(message, payload, compare_distance=0):
    min_distance = message.text
    valid_min_distance = check_distance(message.from_user.id, min_distance, min_distance_step, payload)
    if valid_min_distance:
        msg = bot.send_message(message.from_user.id,
                               "Теперь необходимо указать максимальное расстояние отеля от центра:")
        bot.register_next_step_handler(msg, max_distance_step, payload, valid_min_distance)


def max_distance_step(message, payload, min_distance):
    max_distance = message.text
    valid_max_distance = check_distance(message.from_user.id, max_distance, max_distance_step, payload,
                                        compare_distance=min_distance)
    if valid_max_distance:
        payload["distance_range"] = [min_distance, valid_max_distance]
        msg = bot.send_message(message.from_user.id, "Отлично, теперь укажите необходимое количество отелей на "
                                                     "вывод (не более 30).", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, hotels_counting, payload)
