from loader import bot
from functions.number_check import number_check
from functions.kid_age_checker import kid_age_checker
from functions.kids_ages_saver import kids_ages_saver
from functions.guests_flag_saver import guests_flag_saver


def number_of_kids(message):
    valid_kids_number = number_check(message.from_user.id, message.text, number_of_kids)
    if valid_kids_number:
        if valid_kids_number < 1 or valid_kids_number > 6:
            msg = bot.send_message(message.from_user.id, "Количество несовершеннолетних гостей может быть от 1 до 6."
                                                         "Попробуйте еще раз.")
            bot.register_next_step_handler(msg, number_of_kids)
        else:
            msg = bot.send_message(message.from_user.id, "Введите возраст 1-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_1, valid_kids_number)


def kid_age_add_1(message, kids_number):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        if kids_number == 1:
            guests_flag_saver(message.from_user.id)
        else:
            msg = bot.send_message(message.from_user.id, f"Введите возраст 2-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_2, kids_number)


def kid_age_add_2(message, kids_number):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        if kids_number == 2:
            guests_flag_saver(message.from_user.id)
        else:
            msg = bot.send_message(message.from_user.id, f"Введите возраст 3-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_3, kids_number)


def kid_age_add_3(message, kids_number):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        if kids_number == 3:
            guests_flag_saver(message.from_user.id)
        else:
            msg = bot.send_message(message.from_user.id, f"Введите возраст 4-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_4, kids_number)


def kid_age_add_4(message, kids_number):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        if kids_number == 4:
            guests_flag_saver(message.from_user.id)
        else:
            msg = bot.send_message(message.from_user.id, f"Введите возраст 5-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_5, kids_number)


def kid_age_add_5(message, kids_number):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        if kids_number == 5:
            guests_flag_saver(message.from_user.id)
        else:
            msg = bot.send_message(message.from_user.id, f"Введите возраст 6-го ребенка:")
            bot.register_next_step_handler(msg, kid_age_add_6, kids_number)


def kid_age_add_6(message):
    current_kid_age = message.text
    valid_kid_age = kid_age_checker(current_kid_age, message.from_user.id)
    if valid_kid_age:
        kids_ages_saver(valid_kid_age, message.from_user.id)
        guests_flag_saver(message.from_user.id)
