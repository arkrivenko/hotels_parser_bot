import telebot
from config_data import config

bot = telebot.TeleBot(token=config.TELEGRAM_TOKEN)
