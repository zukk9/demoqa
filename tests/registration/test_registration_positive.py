import time
import pytest
from test_main import RegistrationPage
from conftest import COMBINATIONS

@pytest.mark.parametrize("firstName, lastName, gender, mobileNumber", COMBINATIONS)
def test_registration(browser, firstName, lastName, gender, mobileNumber):
    try:
        registration_page = RegistrationPage(browser)
        registration_page.open()
        registration_page.get_first_name_field().send_keys(firstName)
        registration_page.get_last_name_field().send_keys(lastName)
        registration_page.get_mobile_Number_field().send_keys(mobileNumber)
        registration_page.get_gender_radio_button(gender).click()
        registration_page.submit_form()

    except Exception as e:
        print(f"Test Failed: {str(e)}")

'''
class TestRegistrationPositiveCases:
    @pytest.mark.parametrize("firstName, lastName, gender, mobileNumber", COMBINATIONS)
    def test_valid_registration_min(self, browser, firstName, lastName, gender, mobileNumber):
        main_positive_function(browser, firstName, lastName, gender, mobileNumber)

'''

'''
    # def test_valid_registration_full(self, browser, firstName, lastName, gender, mobileNumber):
    #    main_positive_function(browser, firstName, lastName, gender, mobileNumber)
    def test_valid_registration_min(self, browser, firstName, lastName, gender, mobileNumber):
        browser.get(LINK)

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
    '''






