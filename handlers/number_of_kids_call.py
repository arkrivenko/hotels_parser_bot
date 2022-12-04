from loader import bot
from functions.number_of_kids import number_of_kids


@bot.callback_query_handler(func=lambda call: call.data == "have_kids")
def number_of_kids_call(call):
    msg = bot.send_message(call.from_user.id, "Укажите(числом) количество несовершеннолетних гостей (от 1 до 6).")
    bot.register_next_step_handler(msg, number_of_kids)
