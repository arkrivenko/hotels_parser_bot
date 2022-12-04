from loader import bot
from datetime import datetime


def check_date(user_id, date, func_name):
    try:
        valid_date = datetime.strptime(date, '%d.%m.%Y').date()
    except Exception:
        msg = bot.send_message(user_id, "Проверьте корректность указанной даты и попробуйте еще раз!")
        bot.register_next_step_handler(msg, func_name)
    else:
        return valid_date
