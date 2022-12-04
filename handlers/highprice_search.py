from loader import bot


@bot.callback_query_handler(func=lambda call: call.data == "highprice_button")
@bot.message_handler(commands=["highprice"])
def highprice_search(message):
    bot.send_message(message.from_user.id, "highprice")
