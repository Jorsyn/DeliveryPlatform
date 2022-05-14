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

    def accept_popup(self):
        self.click_elemtent_by(Locators.popup_xpath, By.XPATH)

    def choose_happy_path(self):
        self.click_elemtent_by(Locators.try_scenario_button_id, By.ID)
        self.click_elemtent_by(Locators.scenario_dropdown_xpath, By.XPATH)
        self.click_elemtent_by(Locators.happy_path_id, By.ID)
        self.click_elemtent_by(Locators.accept_scenario_id, By.ID)

    def input_pickup_location(self, text):
        WebDriverWait.until(EC.invisibility_of_element_located((By.ID, Locators.accept_scenario_id)))
        self.select_first_item_dropdown(text, Locators.pickup_location_id, By.ID)

    def input_dropoff_location(self, text):
        self.select_first_item_dropdown(text, Locators.dropoff_location_id, By.ID)
