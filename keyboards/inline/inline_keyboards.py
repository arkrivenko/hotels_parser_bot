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

markup_searching_types = InlineKeyboardMarkup()
markup_searching_types.add(InlineKeyboardButton("Самые дешёвые отели", callback_data="lowprice_button"))
markup_searching_types.add(InlineKeyboardButton("Самые дорогие отели", callback_data="highprice_button"))
markup_searching_types.add(InlineKeyboardButton("Лучшие предложения", callback_data="bestdeal_button"))
markup_searching_types.add(InlineKeyboardButton("История поиска", callback_data="history_button"))

markup_get_history = InlineKeyboardMarkup()
markup_get_history.add(InlineKeyboardButton("За сутки", callback_data="for_a_day"))
markup_get_history.add(InlineKeyboardButton("За неделю", callback_data="for_a_week"))
markup_get_history.add(InlineKeyboardButton("За месяц", callback_data="for_a_month"))
markup_get_history.add(InlineKeyboardButton("За всё время", callback_data="for_all_time"))
