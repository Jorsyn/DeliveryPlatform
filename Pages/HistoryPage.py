import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import Resources.Locators as Locators
import Pages.BasePage as BasePage
import Resources.TestData as TestData


class HistoryPage(BasePage.BasePage):

    def select_job(self, jobID):
        self.click_elemtent_by(Locators.job_appendable_id + jobID, By.ID)

    def validate_pickup_location(self):
        self.validate_location(TestData.pickup_location, Locators.pickup_address_id, By.ID)

    def validate_dropoff_location(self):
        self.validate_location(TestData.dropoff_location, Locators.dropoff_address_id, By.ID)


    def validate_delivery_distance(self):
        print("Distance should be greater than zero")
        self.validate_number_greater_than_o(Locators.distance_xpath, By.XPATH)

    def validate_total_amount(self):
        print("Total amount should be greater than zero")
        item = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, Locators.total_amount_xpath)))
        number = item.text.replace("€","")
        print("Number is:", number)
        assert float(number) > 0

    def validate_invoice_downloadable(self):
        print("Invoice should be available and clickable")
        self.click_elemtent_by(Locators.invoice_link_xpath, By.XPATH)

    def validate_pdf_title(self):
        url = self.driver.current_url
        bucket_url = "https://stuart-bucket-sandbox.s3"
        print("URL should be in the correct domain:", bucket_url)
        assert bucket_url in url
