from loader import bot
from telebot.types import ReplyKeyboardRemove
from city_input import city_input
from hotels_counting import hotels_counting


def pre_hotels_counting(message, cities_dict, payload):
    selected_city = message.text
    if selected_city not in cities_dict.keys():
        msg = bot.send_message(message.from_user.id, "Город не распознан. Введите его заново:")
        bot.register_next_step_handler(msg, city_input, payload)
    else:
        selected_city_id = cities_dict.get(selected_city)
        payload["destination"]["regionId"] = selected_city_id
        msg = bot.send_message(message.from_user.id, "Отлично, теперь укажите необходимое количество отелей на вывод"
                                                     " (не более 30).", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, hotels_counting, payload)
