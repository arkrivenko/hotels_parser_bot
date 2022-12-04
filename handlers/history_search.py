from loader import bot


@bot.callback_query_handler(func=lambda call: call.data == "history_button")
@bot.message_handler(commands=["history"])
def history_search(message):
    bot.send_message(message.from_user.id, "history")
