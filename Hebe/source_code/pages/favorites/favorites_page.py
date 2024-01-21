import allure

from Hebe.source_code.pages.base_element import BaseElement
from Hebe.source_code.pages.base_page import BasePage


class FavoritesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.products_in_favorites = BaseElement(driver, "//*[@class='product-tile   js-product-tile  ']")
        self.removed_product = BaseElement(driver, "(//*[@class='product-tile   js-product-tile  '])[2]")
        self.favorites_heart_button = BaseElement(driver,
                                                  "(//*[@class='wishlist-icon__svg wishlist-icon__svg--full'])[1]")

        self.empty_favorites_notification = BaseElement(driver, "//*[@class='wishlist__msg-empty']")

    @allure.step('Delete product from favorites')
    def delete_product(self):
        self.favorites_heart_button.click()
