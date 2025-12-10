from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.pin_code_input = (By.ID, "postal-code")
        self.button_click_input = (By.ID, "continue")
        self.item_total_input = (By.CSS_SELECTOR, ".summary_subtotal_label")
        self.tax_input = (By.CSS_SELECTOR, ".summary_tax_label")
        self.amount_input = (By.CSS_SELECTOR, ".summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.purchase_message = (By.CLASS_NAME, "complete-header")
        self.problem_message = (By.CSS_SELECTOR,"h3[data-test='error']")
        self.home_message = (By.ID,"back-to-products")


    def standard_personal_info(self, first_name, last_name, pin_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.pin_code_input).send_keys(pin_code)
        self.driver.find_element(*self.button_click_input).click()


    def problem_personal_info(self, first_name, last_name, pin_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.pin_code_input).send_keys(pin_code)
        self.driver.find_element(*self.button_click_input).click()
        problem_error = self.driver.find_element(*self.problem_message).text
        assert "Last Name is required" in problem_error

    def error_personal_info(self, first_name, pin_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.pin_code_input).send_keys(pin_code)
        self.driver.find_element(*self.button_click_input).click()


    def price_validation(self):
        # Price Validation
        item_total_text = self.driver.find_element(*self.item_total_input).text
        item_total = float(item_total_text.split("$")[1])
        tax_text = self.driver.find_element(*self.tax_input).text
        tax = float(tax_text.split("$")[1])
        total_amount = float(tax + item_total)
        amount_text = self.driver.find_element(*self.amount_input).text
        amount = float(amount_text.split("$")[1])
        if round(total_amount, 2) == round(amount, 2):
            print("The price is validated")
        else:
            print("Error in price validation")
        self.driver.find_element(*self.finish_button).click()


    def purchase_success(self):
        # Final order successful message
        message = self.driver.find_element(*self.purchase_message).text
        assert "Thank you" in message
        back_to_home = self.driver.find_element(*self.home_message).click()
