import allure

from Hebe.source_code.pages.base_element import BaseElement
from Hebe.source_code.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.email_field = BaseElement(driver, "//*[@type='email']")
        self.password_field = BaseElement(driver, "//*[@type='password']")
        self.name_field = BaseElement(driver, "//*[@id='dwfrm_profile_customer_firstname']")
        self.lastname_field = BaseElement(driver, "//*[@id='dwfrm_profile_customer_lastname']")
        self.phone_field = BaseElement(driver, "//*[@type='tel']")
        self.checkbox = BaseElement(driver, "(//*[@class='checkbox-label checkbox-label--registration'])[1]")
        self.submit_button = BaseElement(driver, "//*[@type='submit']")
        self.registration_message = BaseElement(driver, "//*[@class='confirmation-card__title']")
        self.email_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_email-error']")
        self.password_error_message = BaseElement(driver,
                                                  "//*[@class='form-aside-validation__item js-list-password-validation error']")
        self.name_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_firstname-error']")
        self.lastname_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_lastname-error']")
        self.phone_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_phoneMobile-error']")

    @allure.step('Make registration')
    def make_registration(self, email, password, first_name, last_name, phone_number):
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.name_field.send_keys(first_name)
        self.lastname_field.send_keys(last_name)
        self.phone_field.send_keys(phone_number)
        self.checkbox.custom_click()
        self.submit_button.custom_click()
        self.checkbox.wait_until_invisibility()
