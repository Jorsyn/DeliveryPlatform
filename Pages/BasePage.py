import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import Resources.Locators as Locators

class BasePage():
    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def navigate_to(self, page):
        self.driver.get(page)

    def accept_popup(self):
        self.click_elemtent_by(Locators.popup_xpath, By.XPATH)


    def choose_happy_path(self):
        self.click_elemtent_by(Locators.try_scenario_button_id, By.ID)
        self.click_elemtent_by(Locators.scenario_dropdown_xpath, By.XPATH)
        self.click_elemtent_by(Locators.happy_path_id, By.ID)
        self.click_elemtent_by(Locators.accept_scenario_id, By.ID)

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


    def validate_location(self, address, element, by):
        location = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((by, element)))
        print("Location should match:", address, "\nLocation found:", location.text)
        assert location.text == address

    def validate_number_greater_than_o(self, element, by):
        item = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((by, element)))
        print("Number is:", item.text)
        assert float(item.text) > 0



