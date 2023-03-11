# pytest -v -m login_user --tb=line --language=en test_disk_page.py
# pytest -v -s -m login_user test_disk_page.py

import pytest, os, time
from .pages.login_page import FlashLoginPage, LoginPage
from .pages.main_page import MainPage
from .pages.disk_page import DiskPage
from .pages.locators import DiskPageLocators

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

    @pytest.mark.skip
    @pytest.mark.yandex_disk_part_1
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

        page.go_to_disk_root_dir()  # выход наружу

        # Создание каталога
        page.should_be_button_create()
        page.go_to_button_create()

        page.should_be_dir_plus()
        page.go_to_dir_plus()
        ####page.go_to_dir_plus_perform()

        dir_name = 'SDET_UI_Dir_1'
        page.should_be_dialog_form()
        page.create_obj(dir_name)

        # Вход в папку
        #page.get_list_objects()
        page.should_be_disk_obj_name(dir_name)
        page.go_to_inside_dir(dir_name)
        time.sleep(3)

        # Создание файла
        page.should_be_button_create()
        page.go_to_button_create()
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
        page.should_be_disk_obj_name(file_name)

        # Разлогиниваемся
        page.go_to_logout()


    @pytest.mark.skip
    @pytest.mark.yandex_disk_part_2
    def test_yandex_disk_page_2(self, browser):
        # Яндекс Дик
        link = LINK_DISK
        page = DiskPage(browser, link, timeout=10)
        page.open()
        #if page.is_ad_flash_show():
        #    page.go_to_close_ad_flash()
        page.should_be_authorized_user()  # пользователь залогинен
        #page.go_to_hide_profile()
        # time.sleep(5)

        page.go_to_disk_root_dir()  # выход наружу - левый клик

        # Создание каталога
        page.should_be_button_create()
        page.go_to_button_create()

        page.should_be_dir_plus()
        page.go_to_dir_plus()
        ####page.go_to_dir_plus_perform()

        dir_name2 = 'SDET_UI_Dir_2'
        page.should_be_dialog_form()
        page.create_obj(dir_name2)
        time.sleep(1)

        if page.is_dlg_show():
            page.go_to_dialog_close_click()

        page.go_to_disk_root_dir()  # выход наружу

        # Проверяем наличие файла
        file_name = DiskPageLocators.FILE_FOR_COPY
        page.should_be_disk_obj_name(file_name)
        # по идее if поставить и не делать ничего, если файла нет
        page.go_to_disk_file_click(file_name)
        #time.sleep(1)

        page.should_be_top_button_info()
        page.should_be_top_button_copy()
        #page.scroll_to_top_button_copy()
        page.go_to_top_button_copy()

        #page.go_to_dlg_root_dir()
        page.should_be_dlg_obj_name(dir_name2)
        page.go_to_dlg_dir_select(dir_name2)
        page.go_to_dlg_button_copy()
        #time.sleep(1)
        page.go_to_disk_root_dir()

        # Вход в папку 2
        #page.get_list_objects()
        page.should_be_disk_obj_name(dir_name2)
        page.go_to_inside_dir(dir_name2)
        time.sleep(3)

        # Проверка имени файла
        page.should_be_disk_obj_name(file_name)

        # Разлогиниваемся
        page.go_to_logout()

    @pytest.mark.skip
    @pytest.mark.yandex_disk_part_3
    def test_yandex_disk_page_3(self, browser):
        # Яндекс Дик
        link = LINK_DISK
        page = DiskPage(browser, link, timeout=10)
        page.open()
        #if page.is_ad_flash_show():
        #    page.go_to_close_ad_flash()
        page.should_be_authorized_user()  # пользователь залогинен
        #page.go_to_hide_profile()
        # time.sleep(5)

        page.go_to_disk_root_dir()  # выход наружу

        # Проверяем наличие файла
        file_name = DiskPageLocators.FILE_FOR_COPY
        page.should_be_disk_obj_name(file_name)
        # по идее if поставить и не делать ничего, если файла нет
        # Копируем файл
        page.go_to_disk_file_click(file_name)
        page.should_be_top_button_copy()
        page.go_to_top_button_copy()

        dir_name1 = 'SDET_UI_Dir_1'
        page.should_be_dlg_obj_name(dir_name1)
        page.go_to_dlg_dir_select(dir_name1)
        page.go_to_dlg_button_copy()
        #time.sleep(1)
        #page.go_to_disk_root_dir() # выход наружу

        # Вход в папку 1
        page.should_be_disk_obj_name(dir_name1)
        page.go_to_inside_dir(dir_name1)
        time.sleep(3)

        # Удаление лишних файлов - del_other_files
        #page.id_item_objects() # cheker
        #page.id_item_object(file_name) # cheker
        page.del_list_objects_except(file_name)

          # Проверка имени файла
        page.should_be_disk_obj_name(file_name)

        # Разлогиниваемся
        page.go_to_logout()


    @pytest.mark.yandex_disk_part_4
    def test_yandex_disk_page_4(self, browser):
        # Яндекс Дик
        link = LINK_DISK
        page = DiskPage(browser, link, timeout=10)
        page.open()
        page.should_be_authorized_user()  # пользователь залогинен

        page.go_to_disk_root_dir()  # выход наружу - левый клик

        # Создание каталога
        page.should_be_button_create()
        page.go_to_button_create()

        page.should_be_dir_plus()
        page.go_to_dir_plus()
        ####page.go_to_dir_plus_perform()

        dir_name4 = 'SDET_UI_Dir_4'
        file_name = DiskPageLocators.FILE_FOR_UPLOAD

        page.should_be_dialog_form()
        page.create_obj(dir_name4)
        time.sleep(1)

        if page.is_dlg_show():
            page.go_to_dialog_close_click()

        # Вход в папку
        page.should_be_disk_obj_name(dir_name4)
        page.go_to_inside_dir(dir_name4)
        time.sleep(3)

        # Загрузка файла - нажатие на кнопку
        #page.should_be_button_upload()
        #page.go_to_button_upload()

        # Загрузка файла - через input type=file
        page.should_be_input_file()
        home_dir = os.path.expanduser("~")
        full_path = os.path.join(home_dir, DiskPageLocators.FILE_FOR_UPLOAD)
        if os.path.exists(full_path):
            page.put_file_path_to_input_upload(full_path)
            time.sleep(3)

            # Проверка имени файла
            page.should_be_disk_obj_name(file_name)

        # Разлогиниваемся
        page.go_to_logout()
