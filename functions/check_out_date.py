from loader import bot
from keyboards.inline.inline_keyboards import markup_check_out, markup_searching_types
from database.database_functions import get_check_in_date, set_check_out_date, set_dates_flag, get_guests_count_flag
from functions.check_date import check_date


def check_out_date(message):
    input_date = message.text
    check_in_date = get_check_in_date(message.from_user.id)
    valid_date = check_date(message.from_user.id, input_date, check_out_date)
    if valid_date:
        if check_in_date >= valid_date:
            msg = bot.send_message(message.from_user.id, "Дата выезда должна быть больше даты заезда,"
                                                         "попробуйте еще раз!")
            bot.register_next_step_handler(msg, check_out_date)
        else:
            set_check_out_date(valid_date, message.from_user.id)
            set_dates_flag(1, message.from_user.id)
            guests_count_flag = get_guests_count_flag(message.from_user.id)
            if guests_count_flag == 1:
                bot.send_message(message.from_user.id,
                                 "Дата выезда успешно сохранена. Теперь можно переходить к поиску.",
                                 reply_markup=markup_searching_types)
            else:
                bot.send_message(message.from_user.id, "Дата выезда сохранена, теперь необходимо указать количество "
                                                       "гостей.", reply_markup=markup_check_out)
