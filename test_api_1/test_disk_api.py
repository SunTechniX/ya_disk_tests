# pytest -v -m login_user --tb=line test_disk_api.py
# pytest -v -s -m login_user test_disk_api.py

import pytest
import time
from .api.test_api_01 import TestApi_01
from .api.locators import BaseApiLocators
from urllib.parse import urljoin

@pytest.mark.login_user
class TestUserActionsFromAPIYandexDisk():
    @pytest.mark.skip
    @pytest.mark.yandex_disk_part_5
    def test_yandex_disk_page_5(self):
        TestApi5 = TestApi_01()
        print('Список всех файлов (включая вложенные папки):')
        TestApi5.test_list_files()
        print('Список каталогов (с древовидной структурой):')
        TestApi5.test_list_dirs()

    @pytest.mark.skip
    @pytest.mark.yandex_disk_part_6
    def test_yandex_disk_page_6(self):
        TestApi6 = TestApi_01()
        new_path_dir = 'DET_API_Dir_6'
        TestApi6.test_create_dir(new_path_dir)
        print(f'\nСписок каталогов (с каталогом {new_path_dir}):\n')
        TestApi6.test_list_dirs()
        print(f'\nПроверка того, что каталог "{new_path_dir}" удалён:\n')
        TestApi6.test_delete_dir(new_path_dir)
        TestApi6.test_list_dirs()

    @pytest.mark.yandex_disk_part_7
    def test_yandex_disk_page_7(self):
        TestApi7 = TestApi_01()
        new_path_dir = 'SDET_API_Dir_7'
        file_name = BaseApiLocators.FILE_FOR_COPY
        TestApi7.test_create_dir(new_path_dir)
        TestApi7.test_obj_exist(file_name)
        TestApi7.test_obj_exist(new_path_dir)
        TestApi7.copy_file('/' + file_name, '/' + new_path_dir + '/' + file_name);

        #TestApi7.test_delete_dir(new_path_dir)
        #TestApi7.test_list_dirs()
