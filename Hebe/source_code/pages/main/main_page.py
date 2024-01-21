import allure
from selenium.webdriver import Keys

from Hebe.source_code.pages.base_element import BaseElement
from Hebe.source_code.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.accept_cookies_button = BaseElement(driver, "//*[@id='onetrust-accept-btn-handler']")
        self.search_string = BaseElement(driver, "//*[@id='q']")
        self.search_results = BaseElement(driver, "//*[@class='product-tile__name']")
        self.registration_icon = BaseElement(driver, "//*[@href='https://www.hebe.pl/account']")
        self.create_account_button = BaseElement(driver, "//*[@title='Załóż konto']")
        self.no_hebe_card_button = BaseElement(driver, "//*[@title='nie mam karty My Hebe']")
        self.first_product = BaseElement(driver, "(//*[@class='product-tile   js-product-tile  '])[1]")
        self.add_to_favorites_button = BaseElement(driver, "(//*[@title='Dodaj do listy życzeń'])[1]")
        self.favorites_quantity_icon = BaseElement(driver, "//*[@class='header-button__badge js-wishlist-quantity']")
        self.favorites_heart_button = BaseElement(driver,
                                                  "(//*[@class='wishlist-icon__svg wishlist-icon__svg--full'])[1]")
        self.put_product_to_cart_button = BaseElement(driver, "//*[@title='DODAJ DO KOSZYKA']")
        self.go_to_cart_button = BaseElement(driver, "//*[@class='button product-set-dialog__button']")
        self.continue_shopping_button = BaseElement(driver, "//*[@class='button button--outline js-close-modal']")
        self.pop_up_window = BaseElement(driver,
                                         "//*[@class='everyday-promo__arrow js-everyday-promo-minimize-trigger']")

    @allure.step('Accept cookies')
    def accept_cookies(self):
        if self.accept_cookies_button.assert_element(clickable=True):
            self.accept_cookies_button.click()

    @allure.step('Find product by search string')
    def find_by_search_string(self, input_word):
        search_string = self.search_string.assert_element(clickable=True)
        search_string.send_keys(input_word)
        search_string.send_keys(Keys.RETURN)

    @allure.step('Go to registration page')
    def go_to_registration_page(self):
        self.registration_icon.hover()
        self.create_account_button.click()
        self.no_hebe_card_button.click()

    @allure.step('Add product to favorites')
    def add_to_favorites(self, input_word):
        self.find_by_search_string(input_word)
        self.first_product.hover()
        self.add_to_favorites_button.click()

    @allure.step('Add product to cart')
    def add_to_cart(self, input_word):
        self.find_by_search_string(input_word)
        self.first_product.click()
        self.put_product_to_cart_button.click()

    @allure.step('Minimize pop-up window on the main page')
    def minimize_pop_up_window(self):
        if self.pop_up_window.assert_element(clickable=True):
            self.pop_up_window.click()
