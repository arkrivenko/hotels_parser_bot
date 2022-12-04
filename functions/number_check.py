from loader import bot


def number_check(user_id, number, func_name):
    if not number.isdecimal():
        msg = bot.send_message(user_id, "Количество гостей должно быть указано в числовом формате (например: 3).\n"
                                        "Попробуйте еще раз:")
        bot.register_next_step_handler(msg, func_name)
    else:
        valid_guests_number = int(number)
        return valid_guests_number
