import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSd7y1QHa2CIJJSv41yt07K_6tf3-emnNcwxfhx5VwuGl8TuTw/viewform?usp=sf_link"

response = requests.get(ZILLOW_CLONE)
zillow_site = response.text
soup = BeautifulSoup(zillow_site, "html.parser")

links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
all_links = [link.get("href") for link in links]
print(all_links)

prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in prices if "$" in price.text]
print(all_prices)

addresses = soup.find_all(name="address")
all_addresses = [address.get_text().strip().replace("|", "") for address in addresses]
print(all_addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for n in range(len(all_links)):
    driver.get(GOOGLE_FORM)
    sleep(1)
    address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address_input.click()
    address_input.send_keys(all_addresses[n])

    price_input.click()
    price_input.send_keys(all_prices[n])

    link_input.click()
    link_input.send_keys(all_links[n])

    submit_button.click()

driver.quit()