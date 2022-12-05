from loader import bot
from functions.pre_city_input import pre_city_input


@bot.callback_query_handler(func=lambda call: call.data == "lowprice_button")
@bot.message_handler(commands=["lowprice"])
def lowprice_search(message):
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
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": 100000,
            "min": 1
        }}
    }
    pre_city_input(payload, message.from_user.id)
