from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"

#enter your twitter username and password

TWITTER_USERNAME = "username"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot:
    def __init__(self):
        service = Service(CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        print("clicked")
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(self.down)
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.up)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div').click()
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_USERNAME)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')

        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label = "Tweet"]').click()
        time.sleep(3)
        tweet_text = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftEditor-content")
        tweet_text.send_keys(f"Hello @jio why is my internet speed {self.down} down/{self.up}up. when I pay for 100 up/100 down")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]').click()
        self.driver.close()


