import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from Pytest.PageObjects.Checkout import CheckoutPage
from Pytest.PageObjects.ShopPage import Shop
from Pytest.PageObjects.login import loginPage

data_path = r'Pytest\Data\Test_Framework.json'
with open(data_path) as f:
    test_data = json.load(f)
    test_valid = test_data["data1"]
    test_locked = test_data["data2"]
    test_problem = test_data["data3"]
    test_glitch = test_data["data4"]
    test_error = test_data["data5"]


@pytest.mark.parametrize("test_list_data1", test_valid)
def test_standarduser(browserinstance, test_list_data1):
    driver = browserinstance
    Login1 = loginPage(driver)
    Login1.standard_login(test_list_data1["username"], test_list_data1["password"])
    ShopPage = Shop(driver)
    ShopPage.add_to_cart(test_list_data1["item-name"])
    ShopPage.go_to_cart()
    checkout1 = CheckoutPage(driver)
    checkout1.standard_personal_info(test_list_data1["first_name"], test_list_data1["last_name"], test_list_data1["pin_code"])
    checkout1.price_validation()
    checkout1.purchase_success()

@pytest.mark.parametrize("test_list_data2", test_locked)
def test_lockeduser(browserinstance, test_list_data2):
    driver = browserinstance
    Login2 = loginPage(driver)
    Login2.locked_login(test_list_data2["username"], test_list_data2["password"])


@pytest.mark.parametrize("test_list_data3", test_problem)
def test_problemuser(browserinstance,test_list_data3):
    driver = browserinstance
    Login3 = loginPage(driver)
    Login3.standard_login(test_list_data3["username"], test_list_data3["password"])
    ShopPage2 = Shop(driver)
    ShopPage2.add_to_cart(test_list_data3["item-name"])
    ShopPage2.go_to_cart()
    checkout2 = CheckoutPage(driver)
    checkout2.problem_personal_info(test_list_data3["first_name"], test_list_data3["last_name"], test_list_data3["pin_code"])

@pytest.mark.parametrize("test_list_data4", test_glitch)
def test_performanceglitch(browserinstance,test_list_data4):
    driver = browserinstance
    Login4 = loginPage(driver)
    Login4.glitch_login(test_list_data4["username"],test_list_data4["password"])
    ShopPage3 = Shop(driver)
    ShopPage3.add_to_cart(test_list_data4["item-name"])
    ShopPage3.go_to_cart()
    checkout3 = CheckoutPage(driver)
    checkout3.standard_personal_info(test_list_data4["first_name"], test_list_data4["last_name"], test_list_data4["pin_code"])
    checkout3.price_validation()
    checkout3.purchase_success()

@pytest.mark.parametrize("test_list_data5", test_error)
def test_erroruser(browserinstance,test_list_data5):
    driver = browserinstance
    Login5 = loginPage(driver)
    Login5.error_login(test_list_data5["username"],test_list_data5["password"])
    ShopPage4 = Shop(driver)
    ShopPage4.add_to_cart(test_list_data5["item-name"])
    ShopPage4.go_to_cart()
    checkout4 = CheckoutPage(driver)
    checkout4.error_personal_info(test_list_data5["first_name"], test_list_data5["pin_code"])
    checkout4.price_validation()


