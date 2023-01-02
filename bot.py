from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        email = bot.find_element(By.TAG_NAME, "input")
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(5)
        password = bot.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typd")
        time.sleep(5)
        for i in range(1, 3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            tweetLinks = [
                i.get_attribute("href")
                for i in bot.find_elements(By.XPATH, "//a[@dir='auto']")
            ]
            filteredLinks = list(filter(lambda x: "status" in x, tweetLinks))
            print(filteredLinks)

            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element(By.XPATH, "//div[@data-testid='like']").click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(10)


user = TwitterBot("USERNAME", "PASSWORD")
user.login()
user.like_tweet("programming")
