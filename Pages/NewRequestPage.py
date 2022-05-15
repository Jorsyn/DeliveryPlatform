import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import Resources.Locators as Locators
import Pages.BasePage as BasePage


class NewRequestPage(BasePage.BasePage):

    def input_pickup_location(self, text):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, Locators.accept_scenario_id)))
        self.select_first_item_dropdown(text, Locators.pickup_location_id, By.ID)

    def input_dropoff_location(self, text):
        self.select_first_item_dropdown(text, Locators.dropoff_location_id, By.ID)

    def select_mode_bike(self):
        time.sleep(3)
        self.hover_to_and_click_element_by(Locators.bike_button_xpath, By.XPATH)
        # self.click_elemtent_by(Locators.bike_button_id, By.ID)

    def start_request(self):
        time.sleep(2)
        self.click_elemtent_by(Locators.request_courier_button, By.ID)

    def validate_ongoing(self):
        print("Number of ongoing requests should be greater than zero")
        self.validate_number_greater_than_o(Locators.number_ongoing_requests_xpath, By.XPATH)

