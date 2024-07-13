from pages.base_page import BasePage
from pages.locators import AuthLocators
import time
import os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://lk.smarthome.rt.ru/"
        driver.get(url)

    def enter_email(self, value):
        email = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)
        email.send_keys(value)

    def enter_number(self, value):
        number = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)
        number.send_keys(value)

    def enter_phone(self, value):
        phone = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)
        phone.send_keys(value)
    #
    '''-----------------------'''

    def enter_pass(self, value):
        password = self.driver.find_element(*AuthLocators.AUTH_PASS)
        password.send_keys(value)

    def enter_pass_confirm(self, value):
        pass_confirm = self.driver.find_element(*AuthLocators.AUTH_PASS_CONFIRM)
        pass_confirm.send_keys(value)

    # def btn_click(self): ##
    #     btn = self.driver.find_element(*AuthLocators.AUTH_BTN)
    #     btn.click()
    #     time.sleep(3)  # ждем реакции

    def open_auth_page(self):
        self.open_page(self.url)
    #

    # def open_auth_page(self, url): ###
    #     self.open_page(url=url)

    def enter_eye_mask(self):
        password_mask = self.driver.find_element(*AuthLocators.AUTH_PASS_MASK)
        assert password_mask.is_displayed(), "Password masking not working"

    def test_forgot_password_links(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_FORGOT_PASS_LINK)
        btn.click()
        time.sleep(3)

    def test_agreement(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_USER_AGREEMENT_LINK)
        btn.click()
        time.sleep(3)

    def test_help(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_HELP_LINK)
        btn.click()
        time.sleep(3)

    def test_empty_password(self):
        password = self.driver.find_element(*AuthLocators.AUTH_PASS)
        password.send_keys()


class AuthRegistration(AuthPage):

    def __init__(self, driver, url="https://lk.smarthome.rt.ru/"):
        self.driver = driver
        self.url = url
        super().__init__(self.driver)

    def enter_city(self, value):
        city = self.driver.find_element(*AuthLocators.AUTH_CITY)
        city.send_keys(value)

    def enter_first_name(self, value):
        first_name = self.driver.find_element(*AuthLocators.AUTH_FIRST_NAME)
        first_name.send_keys(value)

    def enter_last_name(self, value):
        second_name = self.driver.find_element(*AuthLocators.AUTH_LAST_NAME)
        second_name.send_keys(value)

    def enter_email_or_phone(self, value):
        email_or_phone = self.driver.find_element(*AuthLocators.AUTH_EMAIL_OR_PHONE)
        email_or_phone.send_keys(value)

    def registration(self, value):
        enter = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION)
        enter.send_keys(value)

    def click_register_button(self):
        btn_click = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION_BTN)
        btn_click()
        time.sleep(2)

    def open_registration_page(self):
        btn_register = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION)
        time.sleep(5)
        return btn_register
