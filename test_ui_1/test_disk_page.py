# pytest -v -m login_user --tb=line --language=en test_disk_page.py
# pytest -v -s -m login_user test_disk_page.py

import pytest
import time
from .pages.login_page import FlashLoginPage, LoginPage
from .pages.main_page import MainPage
from .pages.disk_page import DiskPage

LINK = "http://yandex.ru/"
LINK_DISK = "http://disk.yandex.ru"

@pytest.mark.login_user
class TestUserActionsFromYandexDiskPage():
    link = LINK

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.delete_all_cookies()
        link = LINK
        page = MainPage(browser, link)
        page.open()
        if page.is_captcha_form_show():
            time.sleep(40)
        page.should_be_flash_login_btn()
        page.go_to_flash_login_page()
        # time.sleep(5)

        flash_login_page = FlashLoginPage(browser, browser.current_url)
        flash_login_page.should_be_flash_login_page()
        flash_login_page.go_to_flash_login_via_yandex()
        # time.sleep(5)

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.go_to_mode_select()
        login_page.go_to_enter_username(username='qa-sdet@yandex.ru')
        login_page.go_to_enter_password(password='qaqaSdet7')
        login_page.if_present_pseudo_button()
        #time.sleep(5)
        login_page.should_be_authorized_user()  # проверить, что пользователь залогинен.

    @pytest.mark.yandex_disk_part_1
    @pytest.mark.this_go
    def test_yandex_disk_page_1(self, browser):
        # Яндекс Дик
        link = LINK_DISK
        page = DiskPage(browser, link, timeout=10)
        page.open()
        #if page.is_ad_flash_show():
        #    page.go_to_close_ad_flash()
        page.should_be_authorized_user()  # пользователь залогинен
        #page.go_to_hide_profile()
        # time.sleep(5)

        # Создание каталога
        page.should_be_create_button()
        page.go_to_create_button()

        page.should_be_dir_plus()
        page.go_to_dir_plus()
        ####page.go_to_dir_plus_perform()

        dir_name = 'SDET_UI_Dir_1'
        page.should_be_dialog_form()
        page.create_obj(dir_name)

        # Вход в папку
        #page.get_list_objects()
        page.should_be_obj_name(dir_name)
        page.go_to_inside_dir(dir_name)
        time.sleep(3)

        # Создание файла
        page.should_be_create_button()
        page.go_to_create_button()
        page.should_be_file_plus()
        page.go_to_file_plus()

        file_name = 'File_text_1'
        page.should_be_dialog_form()
        page.create_obj(file_name)
        time.sleep(5)

        # Закрываем вкладку с открывшимся файлом
        main_tab = page.browser.current_window_handle
        new_tab = browser.window_handles[1] # Получаем новое окно - переключаемся на него
        browser.switch_to.window(new_tab)
        browser.close() # Close the tab or window
        browser.switch_to.window(main_tab)

        time.sleep(3)
        # Проверка имени файла
        file_name += '.docx'
        page.should_be_obj_name(file_name)

        # Разлогиниваемся
        page.go_to_logout()

