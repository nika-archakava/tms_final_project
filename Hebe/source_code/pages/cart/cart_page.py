import allure

from Hebe.source_code.pages.base_element import BaseElement
from Hebe.source_code.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.products_in_cart = BaseElement(driver, "//*[@data-action-field='bp']")
        self.notification_in_cart = BaseElement(driver, "//*[@class='cart-primary__title']")
        self.total_in_cart = BaseElement(driver, "//*[@class='cart-summary-totals__value--thick']")
        self.plus_button = BaseElement(driver,
                                                    "//*[@class='tooltip-trigger quantity-buttons-cart__select js-cart-quantity js-quantity']")
        self.first_product_in_cart = BaseElement(driver, "(//*[@data-action-field='bp'])[1]")
        self.second_product_in_cart = BaseElement(driver, "(//*[@data-action-field='bp'])[2]")
        self.delete_product_from_cart_button = BaseElement(driver, "(//*[@value='Usuń produkt'])[1]")
        self.empty_cart_notification = BaseElement(driver, "//*[@class='cart-empty__title']")

    def total(self):
        total_in_cart_text = self.total_in_cart.text()
        total_in_cart = float(total_in_cart_text.replace(',', '.')[:-3])
        return total_in_cart

    @allure.step('Delete product from cart')
    def delete_product(self):
        self.first_product_in_cart.hover()
        self.delete_product_from_cart_button.click()
