from loader import bot
from config_data.config import headers
from database.database_functions import get_current_request, set_history_data
from functions.get_hotels import get_hotels
import requests


def hotels_finder(number_of_photos, user_id):
    final_headers = {"content-type": "application/json"}
    final_headers.update(headers)
    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = get_current_request(user_id)
    sorter = payload.get("sort")
    price_range = None
    distance_range = None
    hotels_counter = None

    if sorter == "DISTANCE":
        hotels_counter = payload.get("resultsSize")
        price_range = payload.get("price_range")
        distance_range = payload.get("distance_range")
        payload.pop("distance_range")
        payload.pop("price_range")
        payload["resultsSize"] = 100

    response = requests.request("POST", url, json=payload, headers=final_headers)
    data = response.json()
    hotels_data = data.get("data").get("propertySearch").get("properties")
    valid_hotels_dict = {}

    if sorter == "DISTANCE":
        flag = False
        while hotels_counter > 0 and flag is False:
            flag, valid_hotels_dict, hotels_counter = valid_hotels_finder(hotels_data, valid_hotels_dict,
                                                                          hotels_counter, distance_range, price_range)
            payload["resultsStartingIndex"] += 100
            try:
                new_response = requests.request("POST", url, json=payload, headers=final_headers)
                data = new_response.json()
                hotels_data = data.get("data").get("propertySearch").get("properties")
            except Exception:
                break

    else:
        for hotel in hotels_data:
            hotel_dict = valid_hotels_dict_maker(hotel)
            valid_hotels_dict.update(hotel_dict)

    if not valid_hotels_dict:
        bot.send_massage(user_id, "По Вашим критериям ничего не нашлось( Изменить параметры поиска и попробуйте "
                                  "еще раз.")
    else:
        url = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"

        for hotel in valid_hotels_dict:
            payload = {
                "currency": "USD",
                "eapid": 1,
                "locale": "en_US",
                "siteId": 300000001,
                "propertyId": hotel
            }
            response = requests.request("POST", url, json=payload, headers=final_headers)
            data = response.json()
            address = data.get("data").get("propertyInfo").get("summary").get("location").get("address").get("addressLine")
            valid_hotels_dict[hotel]["address"] = address
            tagline = data.get("data").get("propertyInfo").get("summary").get("tagline")
            valid_hotels_dict[hotel]["tagline"] = tagline
            photos_list = []
            count = 0

            for elem in data.get("data").get("propertyInfo").get("propertyGallery").get("images"):
                if count == number_of_photos:
                    break
                photo_url = elem.get("image").get("url")
                caption = elem.get("image").get("description")
                hotel_photo_list = [photo_url, caption]
                photos_list.append(hotel_photo_list)
                count += 1

            valid_hotels_dict[hotel]["photos_list"] = photos_list
        set_history_data(valid_hotels_dict, user_id)
        get_hotels(valid_hotels_dict, user_id)


def valid_hotels_dict_maker(hotel):
    hotel_id = hotel.get("id")
    name = hotel.get("name")
    score = hotel.get("reviews").get("score")
    distance = hotel.get("destinationInfo").get("distanceFromDestination").get("value")
    price_per_night = hotel.get("price").get("displayMessages")[0].get("lineItems")[0].get("price").get(
        "formatted")
    price_total = hotel.get("price").get("displayMessages")[1].get("lineItems")[0].get("value")
    hotel_dict = {hotel_id: {"hotel_name": name,
                             "score": score,
                             "distance": distance,
                             "price per night": price_per_night,
                             "total price": price_total
                             }}
    return hotel_dict


def valid_hotels_finder(hotels_data, valid_hotels_dict, hotels_counter, distance_range, price_range):
    flag = False
    for hotel in hotels_data:
        current_price = hotel.get("price").get("lead").get("amount")
        current_distance = hotel.get("destinationInfo").get("distanceFromDestination").get("value")
        if current_distance > distance_range[1] or hotels_counter == 0 or hotel.get("id") in valid_hotels_dict:
            flag = True
            break
        if distance_range[0] <= current_distance <= distance_range[1] and \
                price_range[0] <= current_price <= price_range[1]:
            hotel_dict = valid_hotels_dict_maker(hotel)
            valid_hotels_dict.update(hotel_dict)
            hotels_counter -= 1
    return flag, valid_hotels_dict, hotels_counter
