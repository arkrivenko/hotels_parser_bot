from loader import bot
from functions.pre_city_input import pre_city_input


@bot.callback_query_handler(func=lambda call: call.data == "highprice_button")
@bot.message_handler(commands=["highprice"])
def highprice_search(message):
    flag = False
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
        "sort": "PRICE_HIGH_TO_LOW",
        "filters": {"price": {
            "max": 300,
            "min": 1
        }}
    }
    pre_city_input(payload, message.from_user.id, flag)
