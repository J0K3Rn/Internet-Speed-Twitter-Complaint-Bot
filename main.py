from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# UPDATE ME
PROMISED_DOWNLOAD = 0
PROMISED_UPLOAD = 0
TWITTER_LOGIN = ""
TWITTER_PASSWORD = ""
TWITTER_USERNAME_OR_PHONE_NUMBER = ""
ISP_TWITTER_AT = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.download = None
        self.upload = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # Let site load
        time.sleep(5)

        speed_test = self.driver.find_element(By.CSS_SELECTOR, "a[class*='js-start-test']")
        speed_test.click()
        # Let speedtest run
        time.sleep(75)

        download_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                  "span[class*='result-data-large number result-data-value download-speed']").text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                "span[class*='result-data-large number result-data-value upload-speed']").text
        service_provider = self.driver.find_element(By.CSS_SELECTOR, "div[class*='result-label js-data-isp']").text

        self.download = float(download_speed)
        self.upload = float(upload_speed)

    def twitter_login(self):
        # Login to Twitter
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        login_prompt = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_prompt.send_keys(TWITTER_LOGIN)

        next_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
        next_button.click()

        time.sleep(5)

        # Phone number or username verification
        try:
            phone_or_username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            phone_or_username.send_keys(TWITTER_USERNAME_OR_PHONE_NUMBER)
            next_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
            next_button.click()
            time.sleep(5)
        except NoSuchElementException:
            pass

        password_prompt = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_prompt.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()

        time.sleep(5)

    def tweet_at_provider(self):

        if self.download >= PROMISED_DOWNLOAD and self.upload >= PROMISED_UPLOAD:
            pass

        message = f"Hey @{ISP_TWITTER_AT}, why is my internet speed {self.download}down/{self.upload}up when I pay for" \
                  f" {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?"
        self.driver.get("https://twitter.com/home")

        time.sleep(5)

        tweet_input = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
        tweet_input.send_keys(message)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

    def close_tab(self):
        self.driver.close()

    def shutdown(self):
        self.driver.quit()


# Env variables pre-check
if PROMISED_DOWNLOAD == 0 or PROMISED_UPLOAD == 0 or TWITTER_LOGIN == '' or TWITTER_PASSWORD == '' or TWITTER_USERNAME_OR_PHONE_NUMBER == '' or ISP_TWITTER_AT == '':
    print("Please update all of the env variables!")
    exit(1)

# Bot setup
bot = InternetSpeedTwitterBot()
bot.twitter_login()

# Main loop
while True:
    bot.get_internet_speed()
    bot.tweet_at_provider()
    time.sleep(300)

bot.shutdown()
