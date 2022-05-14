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
        time.sleep(1)
        dd_input.send_keys(Keys.ARROW_DOWN)
        dd_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        dd_input.send_keys(Keys.ENTER)
        time.sleep(1)

    def hover_to_and_click_element_by(self, element, by):
        item = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((by, element)))
        a = ActionChains(self.driver)
        self.driver.execute_script("arguments[0].click();", item)
        # a.move_by_offset(0,-100)
        # time.sleep(3)
        # a.move_to_element(item).click().click().perform()




