from loader import bot
from functions.pre_city_input import pre_city_input


@bot.message_handler(commands=["bestdeal"])
def bestdeal_search(message):
    flag = True
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": None},
        "checkInDate": {
            "day": None,
            "month": None,
            "year": None
        },
        "checkOutDate": {
            "day": None,
            "month": None,
            "year": None
        },
        "rooms": [
            {
                "adults": None,
                "children": None
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": None,
        "sort": "DISTANCE",
        "filters": {"price": {
            "max": 300,
            "min": 1
        }}
    }
    pre_city_input(payload, message.from_user.id, flag)
