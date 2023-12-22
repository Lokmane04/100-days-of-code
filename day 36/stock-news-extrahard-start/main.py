# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# ## STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
# ## STEP 3: Use https://www.twilio.com
# # Send a seperate message with the percentage change and each article's title and description to your phone number.
#
#
# #Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
#

import requests
from datetime import datetime as dt, timedelta

yesterday = str(dt.now() - timedelta(1)).split()[0]
the_day_before = str(dt.now() - timedelta(2)).split()[0]


def stock_increased(day1, day2):
    """ you must pass yesterday as the first parameter"""
    volume1 = day1['5. volume']
    volume2 = day2['5. volume']
    print(volume1, volume2)
    if volume1 < volume2:
        return False
    percentage_increase = (volume1 - volume2) >= ((volume2 * 5) / 100)
    return percentage_increase


def stock_decreased(day1, day2):
    """ you must pass yesterday as the first parameter"""
    volume1 = int(day1['5. volume'])
    volume2 = int(day2['5. volume'])
    print(volume1, volume2)
    if volume1 > volume2:
        return False
    percentage_decrease = (volume2 - volume1) >= ((volume2 * 5) / 100)
    return percentage_decrease


params = {
    "function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "demo"
}

response = requests.get(url="https://www.alphavantage.co/query", params=params)

response.raise_for_status()
data = response.json()["Time Series (Daily)"]
print('yesterday', data[yesterday], 'the_day_before', data[the_day_before])

if stock_decreased(data[yesterday], data[the_day_before])or stock_increased(data[yesterday], data[the_day_before]):
    print("Get News !! ")
