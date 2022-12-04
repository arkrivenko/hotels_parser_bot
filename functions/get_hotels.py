from loader import bot
from telebot.types import InputMediaPhoto
import requests


def get_hotels(hotels_dict, user_id):
    for hotel in hotels_dict.values():
        medias = [InputMediaPhoto(media_list[0], media_list[1]) for media_list in hotel.get("photos_list")
                  if requests.get(media_list[0]).status_code == 200]
        bot.send_message(user_id, f"{hotel.get('hotel_name')}\nРейтинг: {hotel.get('score')}\n"
                                  f"Расстояние до центра: {hotel.get('distance')}\nЦена за ночь: "
                                  f"{hotel.get('price per night')}\nОбщая цена на выбранные даты: "
                                  f"{hotel.get('total price')}")
        if medias:
            bot.send_media_group(user_id, medias)
