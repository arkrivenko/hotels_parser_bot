from loader import bot
from functions.guests_flag_saver import guests_flag_saver


@bot.callback_query_handler(func=lambda call: call.data == "no_kids")
def no_kids_call(call):
    guests_flag_saver(call.from_user.id)
