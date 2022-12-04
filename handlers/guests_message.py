from loader import bot
from functions.adult_guests_checker import adult_guests_checker


@bot.callback_query_handler(func=lambda call: call.data == "guests_button")
@bot.message_handler(commands=["guests"])
def guests_message(message):
    msg = bot.send_message(message.from_user.id, "Укажите(числом) количество совершеннолетних гостей (от 1 до 14)")
    bot.register_next_step_handler(msg, adult_guests_checker)
