from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.flags_checker import flags_checker
from functions.city_input import city_input
from database.database_functions import get_check_in_date, get_check_out_date, get_kids_ages, get_adults_count


@bot.message_handler(commands=["lowprice"])
def lowprice_search(message):
    markup = InlineKeyboardMarkup()
    if flags_checker(message.from_user.id) == 0:
        check_in = get_check_in_date(message.from_user.id)
        check_out = get_check_out_date(message.from_user.id)
        adults_count = get_adults_count(message.from_user.id)
        kids_list = get_kids_ages(message.from_user.id)
        children = []
        if kids_list:
            valid_kids_ages = [int(elem) for elem in kids_list.split("_")]
            for age in valid_kids_ages:
                child = {"age": age}
                children.append(child)
        payload = {
            "currency": "USD",
            "eapid": 1,
            "locale": "en_US",
            "siteId": 300000001,
            "destination": {"regionId": None},
            "checkInDate": {
                "day": check_in.day,
                "month": check_in.month,
                "year": check_in.year
            },
            "checkOutDate": {
                "day": check_out.day,
                "month": check_out.month,
                "year": check_out.year
            },
            "rooms": [
                {
                    "adults": adults_count,
                    "children": children
                }
            ],
            "resultsStartingIndex": 0,
            "resultsSize": None,
            "sort": "PRICE_LOW_TO_HIGH",
            "filters": {"price": {
                "max": 100000,
                "min": 1
            }}
        }
        msg = bot.send_message(message.from_user.id, "Введите город, в котором будет производиться поиск.")
        bot.register_next_step_handler(msg, city_input, payload)
    elif flags_checker(message.from_user.id) == 1:
        markup.row(InlineKeyboardButton("Выбрать даты заезда/выезда", callback_data="dates_button"))
        bot.send_message(message.from_user.id, "Даты заезда/выезда не указаны!", reply_markup=markup)
    else:
        markup.row(InlineKeyboardButton("Выбрать количество проживающих", callback_data="guests_button"))
        bot.send_message(message.from_user.id, "Количество проживающих не указано!", reply_markup=markup)
