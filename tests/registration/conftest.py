import pytest
from selenium import webdriver
import json
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from itertools import product

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

current_dir = Path(__file__).parent
json_path = current_dir.parent.parent / "data" / "data_registration_negative_cases.json"
json_path_positive = current_dir.parent.parent / "data" / "data_registration_positive_cases.json"
image_path = current_dir.parent.parent / "images" / "photo.png"
LINK = "https://demoqa.com/automation-practice-form"
wait = WebDriverWait(browser, 20)

def load_json_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

data = load_json_data(json_path)
data_positive = load_json_data(json_path_positive)

VALID_DATA = {
    "firstName": "Alice",
    "lastName": "Smith",
    "mobileNumber": "1234567890",
}

NEGATIVE_CASES = [
    {
        "firstName": data[0]["firstName"],
        "lastName": data[0]["lastName"],
        "gender": data[0]["gender"],
        "mobileNumber": data[0]["mobileNumber"]
    }
]

COMBINATIONS = list(product(data_positive[0]['firstName'], data_positive[0]['lastName'], data_positive[0]['gender'], data_positive[0]['mobileNumber']))

COMBINATIONS_data = [
    {
        "firstName": data_positive[0]["firstName"],
        "lastName": data_positive[0]["lastName"],
        "gender": data_positive[0]["gender"],
        "mobileNumber": data_positive[0]["mobileNumber"]
    }
]

