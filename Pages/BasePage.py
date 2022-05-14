import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def navigate_to(self, page):
        self.driver.get(page)

    def click_elemtent_by(self, element, by):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((by, element))).click()

    def send_keys_to_elemtent_by(self, text, element, by):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((by, element))).send_keys(text)


    def select_first_item_dropdown(self, text, element, by):
        dd_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((by, element)))

        dd_input.send_keys(text)
        time.sleep(2)
        dd_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        dd_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        dd_input.send_keys(Keys.ENTER)



