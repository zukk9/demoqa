from itertools import product

import pytest
import json
from pathlib import Path
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

current_dir = Path(__file__).parent
json_path = current_dir.parent.parent / "data" / "data_registration_positive_cases.json"
image_path = current_dir.parent.parent / "images" / "photo.png"
link = "https://demoqa.com/automation-practice-form"

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

combinations = list(product(
    data[0]["firstName"],
    data[0]["lastName"],
    data[0]["gender"],
    data[0]["mobileNumber"]
))

class TestRegistrationPositiveCases:
    @pytest.mark.parametrize("firstName, lastName, gender, mobileNumber", combinations)
    def test_valid_registration_min(self, browser, firstName, lastName, gender, mobileNumber):
        browser.get(link)

        browser.find_element(By.ID, "firstName").send_keys(firstName)
        browser.find_element(By.ID, "lastName").send_keys(lastName)

        gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender' and @value='{gender}']")
        browser.execute_script("arguments[0].click();", gender_radio_button)

        browser.find_element(By.ID, "userNumber").send_keys(mobileNumber)
        btn = browser.find_element(By.ID, "submit")
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        modal_window = browser.find_element(By.CSS_SELECTOR, ".modal.show")
        if modal_window.is_displayed():
            assert modal_window.is_displayed(), "Element found"
        else:
            assert modal_window.is_displayed(), "Element not found"
        time.sleep(5)







