from config_data.config import headers
from database.database_functions import get_current_request, set_history_data
from get_hotels import get_hotels
import requests


def hotels_finder(number_of_photos, user_id):
    final_headers = {"content-type": "application/json"}
    final_headers.update(headers)
    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = get_current_request(user_id)
    response = requests.request("POST", url, json=payload, headers=final_headers)
    data = response.json()
    hotels_data = data.get("data").get("propertySearch").get("properties")
    valid_hotels_dict = {}

    for hotel in hotels_data:
        hotel_id = hotel.get("id")
        name = hotel.get("name")
        score = hotel.get("reviews").get("score")
        distance = hotel.get("destinationInfo").get("distanceFromDestination").get("value")
        price_per_night = hotel.get("price").get("displayMessages")[0].get("lineItems")[0].get("price").get("formatted")
        price_total = hotel.get("price").get("displayMessages")[1].get("lineItems")[0].get("value")
        hotel_dict = {hotel_id: {"hotel_name": name,
                                 "score": score,
                                 "distance": distance,
                                 "price per night": price_per_night,
                                 "total price": price_total
                                 }}
        valid_hotels_dict.update(hotel_dict)

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
