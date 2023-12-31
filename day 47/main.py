import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
BUY_PRICE = 200

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
#
price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('YOUR_SMTP_ADDRESS', port=587) as connection:
        connection.starttls()
        result = connection.login("baslimlokman04@gmail.com", 'your password')
        connection.sendmail(
            from_addr="baslimlokman04@gmail.com",
            to_addrs="lokmanbas999@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )