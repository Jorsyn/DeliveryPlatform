import time
import unittest
from selenium import webdriver
import Pages.LoginPage as LoginPage
import Pages.NewRequestPage as NewRequestPage
import Pages.HistoryPage as HistoryPage
import Resources.TestData as TestData


print("Note: This script requires selenium and google chrome with a version matching a GC webdriver located in PATH to work")
print("Google chrome webdriver version 100 it attached to this project")

landing_page = "https://dashboard.sandbox.stuart.com/"
history_page = "https://dashboard.sandbox.stuart.com/history"


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
        self.page.navigate_to(landing_page)
        self.page.input_email(TestData.email)
        self.page.input_password(TestData.password)
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
        self.page.input_pickup_location(TestData.pickup_location)
        self.page.input_dropoff_location(TestData.dropoff_location)
        self.page.select_mode_bike()
        self.page.start_request()
        self.page.validate_ongoing()
        print('Test case 1 finished successfully')

    def test_2_validate_past_delivery(self):
        self.page = HistoryPage.HistoryPage(self.driver)
        self.page.navigate_to(history_page)
        self.page.select_job(TestData.past_delivery_ID)
        self.page.validate_pickup_location()
        self.page.validate_dropoff_location()
        self.page.validate_delivery_distance()
        self.page.validate_total_amount()
        self.page.validate_invoice_downloadable()
        self.page.validate_pdf_title()

        print('Test case 2 finished successfully')



if __name__ == '__main__':
    unittest.main()