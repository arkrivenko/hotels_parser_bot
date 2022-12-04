import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
SECURE_KEY = os.getenv('SECURE_KEY')
DEFAULT_COMMANDS = (
    ("/help", "Помощь"),
    ("/dates", "Выбор даты заезда/выезда"),
    ("/guests", "Указать количество гостей"),
    ("/lowprice", "Самые дешевые отели"),
    ("/highprice", "Самые дорогие отели"),
    ("/bestdeal", "Лучшие предложения"),
    ("/history", "История поиска")
)
headers = {
    "X-RapidAPI-Key": SECURE_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
