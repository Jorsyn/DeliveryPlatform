from selenium.webdriver.common.by import By

# Assign locators

# Login Page
email_id = "email"
password_id = "password"
login_button_id = "logInButton"

# New Request Page
# TODO remove text search and find identier, can fail in other languages
popup_xpath = "//button[@class='CbaUlvx2 oUMO_2x9']/span[contains(text(),'Entendido')]"
try_scenario_button_id = "ScenarioTooltipTryButton"
scenario_dropdown_xpath = "//div[@class='_1Q4GMvTj _1czKoAYf']/span[@id='-label']"
happy_path_id = "-happyPath"
accept_scenario_id = "ScenarioModalApplyButton"
pickup_location_id = "pickUpCard-0-fields-field-address"
dropoff_location_id = "dropOffCard-0-fields-field-address"
bike_button_xpath = "//input[@id='transport-bike']"
request_courier_button = "requestButton"

