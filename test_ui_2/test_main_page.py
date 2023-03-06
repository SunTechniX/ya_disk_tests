# pytest -v -m "login_guest" --tb=line --language=en test_main_page.py
import pytest
from .pages.login_page import FlashLoginPage, LoginPage
from .pages.main_page import MainPage
import time

LINK = "http://yandex.ru/"

@pytest.mark.login_user
class TestLoginFromMainPage():
    @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link, timeout=10)
        page.open()
        page.should_be_flash_login_btn()
        page.go_to_flash_login_page()
        #time.sleep(5)

        flash_login_page = FlashLoginPage(browser, browser.current_url)
        flash_login_page.should_be_flash_login_page()
        flash_login_page.go_to_flash_login_via_yandex()

        time.sleep(10)

    #pytest.mark.skip
    def test_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link, timeout=10)
        page.open()
        page.should_be_flash_login_btn()
        page.go_to_flash_login_page()
        #time.sleep(5)

        flash_login_page = FlashLoginPage(browser, browser.current_url)
        flash_login_page.should_be_flash_login_page()
        flash_login_page.go_to_flash_login_via_yandex()
        #time.sleep(5)

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.go_to_mode_select()
        login_page.go_to_enter_username(username='qa-sdet@yandex.ru')
        login_page.go_to_enter_password(password='qaqaSdet7')
        login_page.if_present_pseudo_button()

        time.sleep(10)

        login_page.should_be_authorized_user()  # проверить, что пользователь залогинен.
