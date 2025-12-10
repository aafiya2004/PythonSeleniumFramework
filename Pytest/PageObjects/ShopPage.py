from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.elements_name = (By.XPATH, "//div[@class='inventory_list']//a//div")
        self.element_text = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_icon = (By.ID, "checkout")

    def add_to_cart(self, item_name):
        # Adding an item to cart
        elements = self.driver.find_elements(*self.elements_name)
        for element in elements:
            if element.text == item_name:
                self.driver.find_element(*self.element_text).click()

    def go_to_cart(self):
        # Checkout
        self.driver.find_element(*self.cart_icon).click()
        self.driver.find_element(*self.checkout_icon).click()
