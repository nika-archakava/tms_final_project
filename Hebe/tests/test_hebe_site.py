import pytest
import allure


from Hebe.source_code.pages.authorization.authorization_page import AuthorizationPage
from Hebe.source_code.pages.base_helpers import BaseHelpers
from Hebe.source_code.pages.cart.cart_page import CartPage
from Hebe.source_code.pages.favorites.favorites_page import FavoritesPage
from Hebe.source_code.pages.main.main_page import MainPage
from Hebe.source_code.pages.registration.registration_page import RegistrationPage


class TestHebeSite:
    @allure.feature('Main page')
    @allure.story('Search string')
    def test_search_string(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        input_word = 'lash'
        main_page.find_by_search_string(input_word)
        with allure.step('Check that search is performed as expected'):
            search_results = main_page.search_results.assert_element(return_many=True)
            for result in search_results:
                assert input_word in result.text.lower(), f"Текст результата '{result}' не содержит ключевое слово '{input_word}'"

    @allure.feature('Registration')
    @allure.story('Registration with valid data')
    def test_user_registration(self, driver):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        base_helpers = BaseHelpers()
        email, password, first_name, last_name, phone_number = base_helpers.generate_random_data()
        registration_page.make_registration(email, password, first_name, last_name, phone_number)
        with allure.step('Check the registration is performed sucessfully'):
            assert registration_page.registration_message.text() == 'Udało Ci się założyć konto!', \
                f'Регистрация не пройдена. Попробуйте еще раз!'
        base_helpers.save_credentials(email, password)

    @allure.feature('Registration')
    @allure.story('Validation of email field')
    @pytest.mark.parametrize('invalid_email',
                             ['@gmail.com', '!@gmail.com', 'nikagmail.com', 'nika@.com', 'nika@q!q.com',
                              'nika@gmailcom', 'nika@gmail.', 'nika@gmail.com1', 'nika@gmail.co!', 'nika@gmail.q'])
    def test_validation_email_field_in_registration(self, driver, invalid_email):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        with allure.step('Enter an invalid data in the email field'):
            registration_page.email_field.send_keys(invalid_email)
        registration_page.password_field.click()
        with allure.step('Ensure that error message is displayed'):
            assert registration_page.email_error_message.text() == 'Podany adres e-mail jest nieprawidłowy, proszę nie używać znaków diakrytycznych, przerw (spacja), ani znaków specjalnych.'

    @allure.feature('Registration')
    @allure.story('Validation of password field')
    @pytest.mark.parametrize('invalid_password,expected_error_message',
                             [['hyujki1!', 'Wielka litera'], ['Hariboi1', 'Cyfra i znak specjalny'],
                              ['Hariboi!', 'Cyfra i znak specjalny'], ['DAREKI1!', 'Mała litera'],
                              ['Darek1!', 'Minimum 8 znaków']])
    def test_validation_password_field_in_registration(self, driver, invalid_password, expected_error_message):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        with allure.step('Enter an invalid data in the password field'):
            registration_page.password_field.send_keys(invalid_password)
        registration_page.name_field.click()
        with allure.step('Ensure that error message is displayed'):
            assert registration_page.password_error_message.text() == expected_error_message

    @allure.feature('Registration')
    @allure.story('Validation of name field')
    @pytest.mark.parametrize('invalid_name', ['f1', 'F!'])
    def test_validation_name_field_in_registration(self, driver, invalid_name):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        with allure.step('Enter an invalid data in the name field'):
            registration_page.name_field.send_keys(invalid_name)
        registration_page.lastname_field.click()
        with allure.step('Ensure that error message is displayed'):
            assert registration_page.name_error_message.text() == 'Pole nie może zawierać cyfr oraz znaków specjalnych.'

    @allure.feature('Registration')
    @allure.story('Validation of last name field')
    @pytest.mark.parametrize('invalid_lastname , expected_error_message',
                             [['a5', 'Pole nie może zawierać cyfr oraz znaków specjalnych.'],
                              ['a!', 'Pole nie może zawierać cyfr oraz znaków specjalnych.']])
    def test_validation_lastname_field_in_registration(self, driver, invalid_lastname, expected_error_message):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        with allure.step('Enter an invalid data in the last name field'):
            registration_page.lastname_field.send_keys(invalid_lastname)
        registration_page.name_field.click()
        with allure.step('Ensure that error message is displayed'):
            assert registration_page.lastname_error_message.text() == expected_error_message

    @allure.feature('Registration')
    @allure.story('Validation of number field')
    @pytest.mark.parametrize('invalid_number', ['1234567', '123f56788', '12345678!'])
    def test_validation_number_field_in_registration(self, driver, invalid_number):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        main_page.accept_cookies()
        main_page.go_to_registration_page()
        with allure.step('Enter an invalid data in the phone number field'):
            registration_page.phone_field.send_keys(invalid_number)
        registration_page.name_field.click()
        with allure.step('Ensure that error message is displayed'):
            assert registration_page.phone_error_message.text() == 'Numer telefonu powinien składać się z ciągu dziewięciu cyfr bez znaków specjalnych'

    @allure.feature('Authorization')
    @allure.story('User authorization with valid data')
    def test_user_authorization(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        with allure.step('Go to authorization window'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        with allure.step('Ensure that authorization is performed sucessfully'):
            assert authorization_page.welcome_string.text() == "Zamówienia", f'Регистрация не прошла!'

    @allure.feature('Authorization')
    @allure.story('User authorization with invalid data')
    @pytest.mark.parametrize('user_login, user_password', [['violataranova@gmail1.com', 'Viola123!'],
                                                           ['violataranova@gmail.com', '12345678']])
    def test_user_authorization_with_invalid_data(self, driver, user_login, user_password):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        with allure.step('Go to authorization window'):
            main_page.registration_icon.click()
        authorization_page.make_authorization(user_login, user_password)
        with allure.step('Ensure that error message is displayed'):
            assert authorization_page.error_message.text() == 'Login lub hasło nie zostało rozpoznane. Spróbuj ponownie.'

    @allure.feature('Favorites')
    @allure.story('Add product to favorites')
    def test_add_to_favorites(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        favorite_page = FavoritesPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        with allure.step('Go to authorization page'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        main_page.add_to_favorites('lash')
        with allure.step('Ensure that quantity of products in favorites is displayed as expected'):
            assert main_page.favorites_quantity_icon.text() == '1', f'Количество товаров в Избранном отображается некорректно!'
        with allure.step('Ensure that favorites heart button color is pink'):
            favorites_heart_button_color = main_page.favorites_heart_button.extract_css_property_of_element('fill')
            assert favorites_heart_button_color == 'rgb(232, 0, 128)', f'Цвет элемента "Сердечко" не соответствует ожидаемому'
        with allure.step('Go to favorites page'):
            main_page.favorites_quantity_icon.click()
        with allure.step('Ensure that product is added to favorites'):
            favorite_page.products_in_favorites.assert_element()
        favorite_page.delete_product()

    @allure.feature('Favorites')
    @allure.story('Delete product from favorites')
    def test_delete_from_favorites(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        favorite_page = FavoritesPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        with allure.step('Go to authorization page'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        main_page.add_to_favorites('lash')
        with allure.step('Clear search string'):
            main_page.search_string.clear()
        main_page.add_to_favorites('lips')
        with allure.step('Go to favorites page'):
            main_page.favorites_quantity_icon.click()
        with allure.step('Ensure that 2 products are added in favorites'):
            products_in_favorites = favorite_page.products_in_favorites.assert_element(return_many=True)
            assert len(products_in_favorites) == 2, f'Ожидалось 2 продукта в Избранном, но обнаружено другое количество'
        favorite_page.delete_product()
        favorite_page.removed_product.wait_until_invisibility()
        with allure.step('Ensure that 1 product is present in favorites'):
            products_in_favorites_2 = favorite_page.products_in_favorites.assert_element(return_many=True)
            assert len(products_in_favorites_2) == 1, "Ожидался 1 продукт в Избранном, но обнаружено другое количество."
        favorite_page.delete_product()
        with allure.step('Ensure that favorites page is empty'):
            assert favorite_page.empty_favorites_notification.text() == 'Na tej liście życzeń nie ma żadnych produktów.'

    @allure.feature('Cart')
    @allure.story('Add product to cart')
    def test_add_to_cart(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        cart_page = CartPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        main_page.minimize_pop_up_window()
        with allure.step('Go to authorization page'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        main_page.add_to_cart('lips')
        with allure.step('Go to cart page'):
            main_page.go_to_cart_button.click()
        with allure.step('Ensure that added product is present in cart'):
            cart_page.products_in_cart.assert_element()
            assert cart_page.notification_in_cart.text() == 'TWÓJ KOSZYK (1 PRODUKT)', f'Текст надписи над товарами не соответствует ожидаемому'
        cart_page.delete_product()
        cart_page.first_product_in_cart.wait_until_invisibility()

    @allure.feature('Cart')
    @allure.story('Change quantity of products in cart')
    def test_change_products_quantity_in_cart(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        cart_page = CartPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        main_page.minimize_pop_up_window()
        with allure.step('Go to authorization page'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        main_page.add_to_cart('lash')
        with allure.step('Go to cart page'):
            main_page.go_to_cart_button.click()
        one_product_price = cart_page.total()
        with allure.step('Click "+" button'):
            cart_page.plus_button.click()
        with allure.step('Ensure that one more product added to cart and total cost are doubled'):
            cart_page.notification_in_cart.wait_text_to_be_present('TWÓJ KOSZYK (2 PRODUKTY)')
            two_products_price = cart_page.total()
            assert two_products_price == one_product_price * 2
        cart_page.delete_product()
        cart_page.first_product_in_cart.wait_until_invisibility()

    @allure.feature('Cart')
    @allure.story('Delete products from cart')
    def test_delete_products_from_cart(self, driver):
        main_page = MainPage(driver)
        authorization_page = AuthorizationPage(driver)
        cart_page = CartPage(driver)
        base_helpers = BaseHelpers()
        main_page.accept_cookies()
        main_page.minimize_pop_up_window()
        with allure.step('Go to authorization page'):
            main_page.registration_icon.click()
        user_email, user_password = base_helpers.load_credentials()
        authorization_page.make_authorization(user_email, user_password)
        main_page.add_to_cart('lips')
        with allure.step('Click "Continue shopping" button'):
            main_page.continue_shopping_button.click()
        main_page.add_to_cart('krem')
        with allure.step('Go to cart page'):
            main_page.go_to_cart_button.click()
        with allure.step('Ensure that 2 products are added to cart'):
            products_in_cart = cart_page.products_in_cart.assert_element(return_many=True)
            assert len(products_in_cart) == 2
        cart_page.delete_product()
        cart_page.second_product_in_cart.wait_until_invisibility()
        with allure.step('Ensure that 1 product is present in cart'):
            products_in_cart_2 = cart_page.products_in_cart.assert_element(return_many=True)
            assert len(products_in_cart_2) == 1, "Ожидался 1 продукт в корзине, но обнаружено другое количество."
        cart_page.delete_product()
        cart_page.first_product_in_cart.wait_until_invisibility()
        with allure.step("Ensure that cart is empty"):
            assert cart_page.empty_cart_notification.text() == 'Twój koszyk jest pusty'
