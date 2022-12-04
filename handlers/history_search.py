from loader import bot


@bot.message_handler(commands=["history"])
def history_search(message):
    bot.send_message(message.from_user.id, "history")
