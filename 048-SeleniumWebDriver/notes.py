from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/LEGO-Expansion-Buildable-Figures-Collectible/dp/B0BSRD1SK5")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")

# Very useful when searching for elements by name. Can also search by ID class, class name, by CSS selector.
# search_bar = driver.find_element(By.NAME, value="q")

# closes the browser
driver.close()

# quits the entire program
# driver.quit()


# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()
