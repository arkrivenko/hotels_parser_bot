from secure_file import TELEGRAM_TOKEN
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Доброго времени суток!")
    elif message.text == "/hello_world":
        bot.send_message(message.from_user.id, "Привет, мир!")


bot.polling(none_stop=True, interval=0)
