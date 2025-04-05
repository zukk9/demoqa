import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from conftest import LINK

class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.url = LINK

    def open(self):
        self.browser.get(self.url)

    def get_first_name_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "firstName")))

    def get_last_name_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "lastName")))

    def get_gender_radio_button(self, gender):
        if gender == "Male":
            gender_value = 1
        elif gender == "Female":
            gender_value = 2
        elif gender == "Other":
            gender_value = 3
        return self.browser.find_element(By.CSS_SELECTOR, f'label[for="gender-radio-{gender_value}"]')

    def get_mobile_Number_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "userNumber")))

    def get_submit_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "submit")))

    def submit_form(self):
        submit_button = self.get_submit_button()
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        submit_button.click()


'''
def main_positive_function(browser, firstName, lastName, mobileNumber, gender):
    browser.get(LINK)
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(firstName)
        wait.until(EC.visibility_of_element_located((By.ID, "lastName"))).send_keys(lastName)
        gender_radio_button = wait.until(EC.visibility_of_element_located((By.XPATH, f"//input[@name='gender']")))
        gender_radio_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, "userNumber"))).send_keys(mobileNumber)
        btn = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        modal_window = wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, ".modal.show"))
        time.sleep(5)
        assert modal_window.is_displayed(), "Modal window is not displayed"
        print("Test Passed: Form Completed with Minimum Fields")

    except Exception as e:
        print(f"Test Failed: {str(e)}")

class TestRegistrationPositiveCases:
    @pytest.mark.parametrize("firstName, lastName, gender, mobileNumber", COMBINATIONS)
    def test_valid_registration_min(self, browser, firstName, lastName, gender, mobileNumber):
        main_positive_function(browser, firstName, lastName, gender, mobileNumber)


def main_positive_function(browser, firstName, lastName, mobileNumber, gender):
    browser.get(LINK)
    browser.find_element(By.ID, "firstName").send_keys(firstName)
    browser.find_element(By.ID, "lastName").send_keys(lastName)

    gender_radio_button = browser.find_element(By.XPATH, f"//input[@name='gender']")
    browser.execute_script("arguments[0].click();", gender_radio_button)
    time.sleep(2)
    browser.find_element(By.ID, "userNumber").send_keys(mobileNumber)
    time.sleep(2)
    btn = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
    btn.click()
    modal_window = browser.find_element(By.CSS_SELECTOR, ".modal.show")
    assert modal_window.is_displayed(), "Modal window is not displayed"
    time.sleep(5)
'''