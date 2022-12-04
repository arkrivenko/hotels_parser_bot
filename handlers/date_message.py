from loader import bot
from datetime import datetime
from functions.check_in_date import check_in_date


@bot.callback_query_handler(func=lambda call: call.data == "dates_button")
@bot.message_handler(commands=["dates"])
def date_message(message):
    current_date = datetime.now().strftime('%d.%m.%Y')
    msg = bot.send_message(message.from_user.id, f"Введите дату заезда в следующем формате:\n"
                                                 f"день.месяц.год (например: {current_date})")
    bot.register_next_step_handler(msg, check_in_date)
