from loader import bot
from functions.hotels_finder import hotels_finder


@bot.callback_query_handler(func=lambda call: call.data == "no_to_hotels_photos")
def no_to_hotels_photos(call):
    hotels_finder(0, call.from_user.id)
