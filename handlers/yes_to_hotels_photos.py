from loader import bot
from functions.photos_counting import photos_counting


@bot.callback_query_handler(func=lambda call: call.data == "yes_to_hotels_photos")
def yes_to_hotels_photos(call):
    msg = bot.send_message(call.from_user.id, "Введите количество фото для вывода (не более 10).")
    bot.register_next_step_handler(msg, photos_counting)
