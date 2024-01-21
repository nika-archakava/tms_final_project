from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def assert_element(self, clickable=False, return_many=False):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath)))

        if clickable:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath)))

        if return_many:
            result = self.driver.find_elements(By.XPATH, self.xpath)
        else:
            result = self.driver.find_element(By.XPATH, self.xpath)

        return result

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.xpath)
        actions.move_to_element(element).perform()

    def click(self):
        element = self.assert_element(clickable=True)
        element.click()

    def custom_click(self):
        element = self.assert_element(clickable=True)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, keys):
        element = self.assert_element(clickable=True)
        element.send_keys(keys)

    def text(self):
        element = self.assert_element()
        return element.text

    def clear(self):
        field = self.assert_element(clickable=True)
        field.clear()

    def extract_css_property_of_element(self, css_property):
        element = self.assert_element()
        css_property_of_element = element.value_of_css_property(css_property)
        return css_property_of_element

    def wait_until_invisibility(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.xpath)))

    def wait_text_to_be_present(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, self.xpath), text))
