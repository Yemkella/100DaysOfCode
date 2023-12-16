import requests
from bs4 import BeautifulSoup
import smtplib

LEGO = "https://www.amazon.com/LEGO-Expansion-Buildable-Figures-Collectible/dp/B0BSRD1SK5"

headers = {
    "Accept-Language": "redacted",
    "User-Agent": "redacted",

}
response = requests.get(url=LEGO, headers=headers)
website = response.content
soup = BeautifulSoup(website, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-price-whole").getText()
price_without_period = price.split(".")[0]
price_float = float(price_without_period)
print(price_float)

if price_float < 100:
    MY_EMAIL = "redacted"
    PASSWORD = "redacted"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="redacted",
            msg=f"Subject: New Low Price! \n\n The lego set you want is under $100! Currently priced at {price_float}! Click here-----> {LEGO}".encode("utf-8")
        )
