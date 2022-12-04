from loader import bot
from keyboards.inline.inline_keyboards import markup_adult_checker
from number_check import number_check
from database.database_functions import set_adults_count


def adult_guests_checker(message):
    valid_adults_number = number_check(message.from_user.id, message.text, adult_guests_checker)
    if valid_adults_number:
        if valid_adults_number < 1 or valid_adults_number > 14:
            msg = bot.send_message(message.from_user.id, "Количество совершеннолетних гостей может быть от 1 до 14. "
                                                         "Попробуйте еще раз.")
            bot.register_next_step_handler(msg, adult_guests_checker)
        else:
            set_adults_count(valid_adults_number, message.from_user.id)
            bot.send_message(message.from_user.id, "Будут ли среди Вас дети?", reply_markup=markup_adult_checker)
