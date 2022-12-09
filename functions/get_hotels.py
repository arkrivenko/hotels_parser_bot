from loader import bot
from telebot.types import InputMediaPhoto
import requests


def get_hotels(hotel_dict, user_id):
    medias = [InputMediaPhoto(media_list[0], media_list[1]) for media_list
              in hotel_dict.get("photos_list")
              if requests.get(media_list[0]).status_code == 200]
    bot.send_message(user_id, f"{hotel_dict.get('hotel_name')}\n"
                              f"Рейтинг: {hotel_dict.get('score')}\n"
                              f"Адрес: {hotel_dict.get('address')}\n"
                              f"Расстояние до центра: {hotel_dict.get('distance')} миль\n"
                              f"Цена за ночь: {hotel_dict.get('price per night')}\n"
                              f"Общая цена с учетом доступных скидок, налогов и сборов: "
                              f"{hotel_dict.get('total price')[:-5]}")
    if medias:
        bot.send_media_group(user_id, medias)
