from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pytest.PageObjects.ShopPage import Shop


class loginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID,"user-name")
        self.password_input = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_message = (By.CSS_SELECTOR,"h3[data-test='error']")
        self.wait_condition = (By.CLASS_NAME,"page_wrapper")

    def standard_login(self,username,password):
         #Entering Username
         self.driver.find_element(*self.username_input).send_keys(username)
         #Entering Password
         self.driver.find_element(*self.password_input).send_keys(password)
         #Clicking the login button
         self.driver.find_element(*self.login_button).click()

    def locked_login(self,username,password):
        # Entering Username
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        error = self.driver.find_element(*self.error_message).text
        print(error)
        assert "locked out" in error.lower(), "Locked user error message not displayed"

    def glitch_login(self,username,password):
         #Entering Username
         self.driver.find_element(*self.username_input).send_keys(username)
         #Entering Password
         self.driver.find_element(*self.password_input).send_keys(password)
         #Clicking the login button
         self.driver.find_element(*self.login_button).click()
         wait = WebDriverWait(self.driver, 10)
         wait.until(expected_conditions.visibility_of_element_located(self.wait_condition))

    def error_login(self,username,password):
        # Entering Username
        self.driver.find_element(*self.username_input).send_keys(username)
        # Entering Password
        self.driver.find_element(*self.password_input).send_keys(password)
        # Clicking the login button
        self.driver.find_element(*self.login_button).click()











