from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database_functions import set_guests_count_flag, get_dates_flag
from keyboards.inline.inline_keyboards import markup_searching_types


def guests_flag_saver(user_id):
    set_guests_count_flag(1, user_id)
    dates_flag = get_dates_flag(user_id)
    if dates_flag == 1:
        bot.send_message(user_id, "Количество гостей успешно сохранено! Можно переходить к поиску.",
                         reply_markup=markup_searching_types)
    else:
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("Выбрать даты заезда/выезда", callback_data="dates_button"))
        bot.send_message(user_id,
                         "Количество гостей успешно сохранено, теперь необходимо указать даты заезда и выезда.",
                         reply_markup=markup)
