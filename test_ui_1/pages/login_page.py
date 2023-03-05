from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import LoginPageLocators


class FlashLoginPage(BasePage):
    def go_to_flash_login_via_yandex(self):
        link = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_FLASH_FORM_BTN_YID))
        #link = self.browser.find_element(*LoginPageLocators.LOGIN_FLASH_FORM_BTN_YID)
        link.click()

    def should_be_flash_login_page(self):
        self.should_be_flash_login_form()
        self.should_be_flash_login_via_yandex_button()

    def should_be_flash_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FLASH_FORM), "Flash Login Form is not presented"

    def should_be_flash_login_via_yandex_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FLASH_FORM_BTN_YID), "Login via Yandex Button is not presented"


class LoginPage(BasePage):
    def go_to_mode_select(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_MODE_BUTTON).click()

    def go_to_enter_username(self, username='any@e.mail'):
        ed_username = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_USER_NAME)
        #ed_username = WebDriverWait(self.browser, 5).until(EC.element_located_to_be_selected(LoginPageLocators.LOGIN_FORM_USER_NAME))
        ed_username.send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_SIGN_IN_BTN).click()

    def go_to_enter_password(self, password='any-password'):
        ed_password = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        #ed_password = WebDriverWait(self.browser, 5).until(EC.element_located_to_be_selected(LoginPageLocators.LOGIN_FORM_PASSWORD))
        ed_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_SIGN_IN_BTN).click()

    #def go_to_pseudo_button_click(self):
    #    self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PSEUDO_BTN).click()

    def if_present_pseudo_button(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_SIGN_IN_BTN).click()
        except:
            pass

        return True

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_login_mode_button()
        self.should_be_login_next_button()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_login_mode_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_MODE_BUTTON), "Mode Button is not presented"

    def should_be_login_next_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_SIGN_IN_BTN), "Sign-in Button is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pass2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        email_field.send_keys(email)
        pass1_field.send_keys(password)
        pass2_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()