import pytest
import json
from pathlib import Path
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

current_dir = Path(__file__).parent
json_path = current_dir.parent.parent / "data" / "data_registration_negative_cases.json"
image_path = current_dir.parent.parent / "images" / "photo.png"
link = "https://demoqa.com/automation-practice-form"

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

valid_data = {
    "firstName": "Alice",
    "lastName": "Smith",
    "mobileNumber": "1234567890",
}
negative_cases = [
    {
        "firstName": data[0]["firstName"],
        "lastName": data[0]["lastName"],
        "gender": data[0]["gender"],
        "mobileNumber": data[0]["mobileNumber"]
    }
]

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

class TestRegistrationNegativeCases:
    @pytest.mark.parametrize("firstName" , negative_cases["firstName"])
    def test_invalid_registration_firstName_min(self, browser, firstName):
        browser.get(link)

        browser.find_element(By.ID, "firstName").send_keys(firstName)
        browser.find_element(By.ID, "lastName").send_keys(valid_data["lastName"])

        gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender']")
        browser.execute_script("arguments[0].click();", gender_radio_button)

        browser.find_element(By.ID, "userNumber").send_keys(valid_data["mobileNumber"])
        btn = browser.find_element(By.ID, "submit")
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        modal_window = browser.find_element(By.CSS_SELECTOR, ".modal.show")
        if modal_window.is_displayed():
            assert modal_window.is_displayed(), "Element found"
        else:
            assert modal_window.is_displayed(), "Element not found"
        time.sleep(5)

    @pytest.mark.parametrize("lastName", negative_cases["lastName"])
    def test_invalid_registration_lastName_min(self, browser, lastName):
            browser.get(link)

            browser.find_element(By.ID, "firstName").send_keys(valid_data["firstName"])
            browser.find_element(By.ID, "lastName").send_keys(lastName)

            gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender']")
            browser.execute_script("arguments[0].click();", gender_radio_button)

            browser.find_element(By.ID, "userNumber").send_keys(valid_data["mobileNumber"])
            btn = browser.find_element(By.ID, "submit")
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            btn.click()
            modal_window = browser.find_element(By.CSS_SELECTOR, ".modal.show")
            if modal_window.is_displayed():
                assert modal_window.is_displayed(), "Element found"
            else:
                assert modal_window.is_displayed(), "Element not found"
            time.sleep(5)

    @pytest.mark.parametrize("mobileNumber", negative_cases["mobileNumber"])
    def test_invalid_registration_mobileNumber_min(self, browser, mobileNumber):
        browser.get(link)
        browser.find_element(By.ID, "firstName").send_keys(valid_data["firstName"])
        browser.find_element(By.ID, "lastName").send_keys(valid_data["lastName"])

        gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender']")
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

        @pytest.mark.parametrize("mobileNumber", negative_cases["mobileNumber"])
        def test_invalid_registration_gender_min(self, browser, mobileNumber):
            browser.get(link)
            browser.find_element(By.ID, "firstName").send_keys(valid_data["firstName"])
            browser.find_element(By.ID, "lastName").send_keys(valid_data["lastName"])

            gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender']")
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



