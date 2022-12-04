from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

markup_start = InlineKeyboardMarkup()
markup_start.row(InlineKeyboardButton("Выбрать даты заезда/выезда", callback_data="dates_button"))
markup_start.row(InlineKeyboardButton("Выбрать количество проживающих", callback_data="guests_button"))

markup_hotels_counting = InlineKeyboardMarkup()
markup_hotels_counting.add(InlineKeyboardButton("Да", callback_data="yes_to_hotels_photos"),
                           InlineKeyboardButton("Нет", callback_data="no_to_hotels_photos"))

markup_check_out = InlineKeyboardMarkup()
markup_check_out.row(InlineKeyboardButton("Выбрать количество проживающих", callback_data="guests_button"))

markup_adult_checker = InlineKeyboardMarkup()
markup_adult_checker.add(InlineKeyboardButton("Да", callback_data="have_kids"),
                         InlineKeyboardButton("Нет", callback_data="no_kids"))
