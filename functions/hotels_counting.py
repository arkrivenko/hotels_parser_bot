from loader import bot
from keyboards.inline.inline_keyboards import markup_hotels_counting
from database.database_functions import set_current_request


def hotels_counting(message, payload):
    number_of_hotels = message.text
    if not number_of_hotels.isdecimal():
        msg = bot.send_message(message.from_user.id, "Количество отелей должно быть указано в виде числа (например: 8)."
                                                     "Попробуйте еще раз.")
        bot.register_next_step_handler(msg, hotels_counting, payload)
    elif int(number_of_hotels) > 30:
        msg = bot.send_message(message.from_user.id, "Количество отелей на вывод не должно превышать 30! "
                                                     "Попробуйте еще раз.")
        bot.register_next_step_handler(msg, hotels_counting, payload)
    else:
        payload["resultsSize"] = int(number_of_hotels)
        set_current_request(payload, message.from_user.id)
        bot.send_message(message.from_user.id, "Необходимо ли выводить фотографии для каждого отеля?",
                         reply_markup=markup_hotels_counting)
