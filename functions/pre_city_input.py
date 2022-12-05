from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.flags_checker import flags_checker
from functions.city_input import city_input
from database.database_functions import get_check_in_date, get_check_out_date, get_kids_ages, get_adults_count


def pre_city_input(payload, user_id):
    markup = InlineKeyboardMarkup()

    if flags_checker(user_id) == 0:
        check_in = get_check_in_date(user_id)
        check_out = get_check_out_date(user_id)
        adults_count = get_adults_count(user_id)
        kids_list = get_kids_ages(user_id)
        children = []

        if kids_list:
            valid_kids_ages = [int(elem) for elem in kids_list.split("_")]
            for age in valid_kids_ages:
                child = {"age": age}
                children.append(child)

        payload["checkInDate"]["day"], payload["checkInDate"]["month"], payload["checkInDate"]["year"] = \
            check_in.day, check_in.month, check_in.year
        payload["checkOutDate"]["day"], payload["checkOutDate"]["month"], payload["checkOutDate"]["year"] = \
            check_out.day, check_out.month, check_out.year
        payload["rooms"][0]["adults"], payload["rooms"][0]["children"] = adults_count, children

        msg = bot.send_message(user_id, "Введите город, в котором будет производиться поиск.")
        bot.register_next_step_handler(msg, city_input, payload)

    elif flags_checker(user_id) == 1:
        markup.row(InlineKeyboardButton("Выбрать даты заезда/выезда", callback_data="dates_button"))
        bot.send_message(user_id, "Даты заезда/выезда не указаны!", reply_markup=markup)

    else:
        markup.row(InlineKeyboardButton("Выбрать количество проживающих", callback_data="guests_button"))
        bot.send_message(user_id, "Количество проживающих не указано!", reply_markup=markup)
