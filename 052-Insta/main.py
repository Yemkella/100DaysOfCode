USERNAME = "REDACTED"
PASSWORD = "REDACTED"

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

class InstaFollower:
    def __init__(self):
        self.driver = driver


    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(4)
        username_input = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.click()
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.click()
        password_input.send_keys(PASSWORD)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        sleep(3.1)

        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        sleep(3)
        self.driver.get("https://www.instagram.com/lego/following")
        sleep(8)
        popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            sleep(2)


    def follow(self):
        follow_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='._aano button')
        for button in follow_buttons:
            try:
                button.click()
                sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()