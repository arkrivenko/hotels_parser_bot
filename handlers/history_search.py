import json
from loader import bot
from keyboards.inline.inline_keyboards import markup_get_history
from functions.get_hotels import get_hotels
from database.database_functions import get_history_data
from datetime import datetime, timedelta


@bot.callback_query_handler(func=lambda call: call.data == "history_button")
@bot.message_handler(commands=["history"])
def history_search(message):
    bot.send_message(message.from_user.id, "Выберите период истории запросов", reply_markup=markup_get_history)


@bot.callback_query_handler(func=lambda call: call.data == "for_a_day")
def for_a_day_call(call):
    starting_day = datetime.now() - timedelta(days=1)
    history = get_history_data(call.from_user.id, starting_day)
    history_data_send(history, call.from_user.id)


@bot.callback_query_handler(func=lambda call: call.data == "for_a_week")
def for_a_week_call(call):
    starting_day = datetime.now() - timedelta(days=7)
    history = get_history_data(call.from_user.id, starting_day)
    history_data_send(history, call.from_user.id)


@bot.callback_query_handler(func=lambda call: call.data == "for_a_month")
def for_a_month_call(call):
    starting_day = datetime.now() - timedelta(days=30)
    history = get_history_data(call.from_user.id, starting_day)
    history_data_send(history, call.from_user.id)


@bot.callback_query_handler(func=lambda call: call.data == "for_all_time")
def for_all_time_call(call):
    history = get_history_data(call.from_user.id)
    history_data_send(history, call.from_user.id)


def history_data_send(history, user_id):
    if history:
        for request in history:
            date = datetime.strptime(request[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d.%m.%Y, %H:%M")
            command = request[1]
            hotels_dict = json.loads(request[2])
            bot.send_message(user_id, f"Была введена следующая команда: {command}\n"
                                      f"Дата и время вызова команды: {date}")
            for hotel in hotels_dict:
                get_hotels(hotels_dict.get(hotel), user_id)
    else:
        bot.send_message(user_id, f"История запросов с Вашего аккаунта не найдена.")
