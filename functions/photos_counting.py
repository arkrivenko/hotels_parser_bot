from loader import bot
from hotels_finder import hotels_finder


def photos_counting(message):
    photos_number = message.text
    if not photos_number.isdecimal():
        msg = bot.send_message(message.from_user.id, "Количество фото должно быть указано в виде числа (например: 3). "
                                                     "Попробуйте еще раз.")
        bot.register_next_step_handler(msg, photos_counting)
    elif int(photos_number) < 2 or int(photos_number) > 10:
        msg = bot.send_message(message.from_user.id, "Количество фото для вывода должно быть от 2 до 10!"
                                                     "Попробуйте еще раз:")
        bot.register_next_step_handler(msg, photos_counting)
    else:
        valid_photos_number = int(photos_number)
        hotels_finder(valid_photos_number, message.from_user.id)
