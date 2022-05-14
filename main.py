import time
import unittest
from selenium import webdriver
import Pages.LoginPage as LoginPage
import Pages.NewRequestPage as NewRequestPage


print("Note: This script requires selenium and google chrome with a version matching a GC webdriver located in PATH to work")
print("Google chrome webdriver version 100 it attached to this project")

landingPage = "https://dashboard.sandbox.stuart.com/"
pickup_location = "58 Avenue Simon Bolivar, 75019 Paris"
dropoff_location = "14 Avenue Simon Bolivar, 75019 Paris"


# TODO remove password and email from here due to security issues in github?
email = "strt.wa+test@gmail.com"
password = "Test!234"


class Tests(unittest.TestCase):
    def setUp(self):
        # Opening the browser
        # This will be the path if you clone the github repository to the default location: home
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        self.page = LoginPage.LoginPage(self.driver)
        self.page.navigate_to(landingPage)
        self.page.input_email(email)
        self.page.input_password(password)
        self.page.click_login_button()
        # assert arriving in new page

    def tearDown(self):
        # Closing the browser
        self.driver.quit()

    def test_1_start_request_happy_path(self):
        print('\nStarting test case 1')
        self.page = NewRequestPage.NewRequestPage(self.driver)
        self.page.accept_popup()
        self.page.choose_happy_path()
        self.page.input_pickup_location(pickup_location)
        self.page.input_dropoff_location(dropoff_location)

        time.sleep(10)
        print('Test case 1 finished successfully')



if __name__ == '__main__':
    unittest.main()