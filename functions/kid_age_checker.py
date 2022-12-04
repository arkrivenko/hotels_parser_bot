from loader import bot


def kid_age_checker(current_age, user_id):
    if not current_age.isdecimal():
        msg = bot.send_message(user_id, "Возраст должен быть указан в числовом формате (например 15). "
                                        "Попробуйте еще раз")
        bot.register_next_step_handler(msg, kid_age_checker)
    elif int(current_age) < 0 or int(current_age) > 17:
        msg = bot.send_message(user_id, "Возраст несовершеннолетнего ребенка не должен превышать 17 лет.")
        bot.register_next_step_handler(msg, kid_age_checker)
    else:
        return current_age
