from loader import bot


@bot.message_handler(commands=["highprice"])
def highprice_search(message):
    bot.send_message(message.from_user.id, "highprice")
