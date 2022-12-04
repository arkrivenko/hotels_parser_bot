from loader import bot
from datetime import datetime
from functions.check_date import check_date
from functions.check_out_date import check_out_date
from database.database_functions import set_check_in_date


def check_in_date(message):
    input_date = message.text
    current_date = datetime.now().date()
    valid_date = check_date(message.from_user.id, input_date, check_in_date)
    if valid_date:
        if current_date > valid_date:
            msg = bot.send_message(message.from_user.id, 'Дата заезда не может быть меньше текущей даты, '
                                                         'попробуйте еще раз!')
            bot.register_next_step_handler(msg, check_in_date)
        else:
            set_check_in_date(valid_date, message.from_user.id)
            msg = bot.send_message(message.from_user.id, "Дата заезда успешно сохранена, теперь введите дату выезда")
            bot.register_next_step_handler(msg, check_out_date)
