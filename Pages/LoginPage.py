import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Resources.Locators as Locators
import Pages.BasePage as BasePage


class LoginPage(BasePage.BasePage):

    def input_email(self, text):
        self.send_keys_to_elemtent_by(text, Locators.email_id, By.ID)

    def input_password(self, text):
        self.send_keys_to_elemtent_by(text, Locators.password_id, By.ID)

    def click_login_button(self):
        self.click_elemtent_by(Locators.login_button_id, By.ID)


