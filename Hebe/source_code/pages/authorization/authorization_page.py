import allure
from selenium.webdriver.support.wait import WebDriverWait

from Hebe.source_code.pages.base_element import BaseElement
from Hebe.source_code.pages.base_page import BasePage


class AuthorizationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.login_field = BaseElement(driver, "//*[@type='email']")
        self.password_field = BaseElement(driver, "//*[@type='password']")
        self.submit_button = BaseElement(driver, "//*[@class='form-row-button pt-15']")
        self.welcome_string = BaseElement(driver, "//*[@class='orders-detail__title']")
        self.error_message = BaseElement(driver, "//*[@class='error-form error-form--marginless']")

    @allure.step('Make an authorization')
    def make_authorization(self, user_login, user_password):
        self.login_field.send_keys(user_login)
        self.password_field.send_keys(user_password)
        self.submit_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
