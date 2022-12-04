from loader import bot
from keyboards.inline.inline_keyboards import markup_start
from database.database_functions import set_start_data


@bot.message_handler(commands=["start", "help"])
def start_message(message):
    set_start_data(message.from_user.id)
    bot.send_message(message.from_user.id, f"Доброго времени суток, <b>{message.from_user.full_name}</b>\n"
                                           "Вас приветствует бот по подбору отелей и хостелов "
                                           "от компании <b>Too Easy Travel</b>!\n\n"
                                           "Для вывода самых дешёвых отелей в городе нажмите: \n/lowprice\n\n"
                                           "Для вывода самых дорогих отелей в городе нажмите: \n/highprice\n\n"
                                           "Для вывода отелей, наиболее подходящих по цене и расположению "
                                           "от центра нажмите: \n/bestdeal\n\n"
                                           "Для вывода истории поиска отелей нажмите: \n/history",
                     parse_mode='html', reply_markup=markup_start)
