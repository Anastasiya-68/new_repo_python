from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    PRODUCT_BACKPACK = (
        By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name"
        )
    PRODUCT_T_SHIRT = (
        By.CSS_SELECTOR, "#item_1_title_link .inventory_item_name"
        )
    PRODUCT_ONESIE = (
        By.CSS_SELECTOR, "#item_2_title_link .inventory_item_name"
        )
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Проверить содержимое корзины
    def product_list(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_BACKPACK, "Sauce Labs Backpack"
                )
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_T_SHIRT, "Sauce Labs Bolt T-Shirt"
                )
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PRODUCT_ONESIE, "Sauce Labs Onesie"
                )
        )

        backpack_text = self.driver.find_element(*self.PRODUCT_BACKPACK).text
        t_shirt_text = self.driver.find_element(*self.PRODUCT_T_SHIRT).text
        onesie_text = self.driver.find_element(*self.PRODUCT_ONESIE).text

        return backpack_text, t_shirt_text, onesie_text

    # Нажать на кнопку Checkout
    def checkout_btn(self):
        checkout_btn = self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BTN)
        )
        checkout_btn.click()
