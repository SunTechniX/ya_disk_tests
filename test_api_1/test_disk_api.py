# pytest -v -m login_user --tb=line test_disk_api.py
# pytest -v -s -m login_user test_disk_api.py

import pytest
from .api.test_api_01 import TestApi_01
from .api.locators import BaseApiLocators


@pytest.mark.login_user
class TestUserActionsFromAPIYandexDisk():
    #pytest.mark.skip
    @pytest.mark.yandex_disk_part_5
    def test_yandex_disk_page_5(self):
        TestApi5 = TestApi_01()
        print('Список всех файлов (включая вложенные папки):')
        TestApi5.files_list('')
        print('Список каталогов (с древовидной структурой):')
        TestApi5.dir_list_discover('/', '')

    #pytest.mark.skip
    @pytest.mark.yandex_disk_part_6
    def test_yandex_disk_page_6(self):
        TestApi6 = TestApi_01()
        new_path_dir = 'SDET_API_Dir6'
        TestApi6.dir_create(new_path_dir)
        print(f'\nСписок каталогов (с каталогом {new_path_dir}):')
        TestApi6.dir_list_discover('/', '')
        print(f'\nПопытка удалить каталог "{new_path_dir}"')
        TestApi6.dir_delete(new_path_dir)
        print(f'\nПроверка того, что каталог "{new_path_dir}" удалён выведем список каталогов:')
        TestApi6.dir_list_discover('/', '')

    @pytest.mark.yandex_disk_part_7
    def test_yandex_disk_page_7(self):
        TestApi7 = TestApi_01()
        new_path_dir = 'SDET_API_Dir7'
        file_name = BaseApiLocators.FILE_FOR_COPY
        file_name_rename = BaseApiLocators.FILE_RENAME
        print(f'\nСоздаём каталог "{new_path_dir}":')
        TestApi7.dir_create(new_path_dir)
        print(f'\nПроверяем, что файл "{file_name}" существует:')
        TestApi7.object_exist(file_name)
        print(f'\nПроверяем, что каталог "{new_path_dir}" существует:')
        TestApi7.object_exist(new_path_dir)
        print(f'\nКопируем файл:')
        TestApi7.file_copy('/' + file_name, '/' + new_path_dir + '/' + file_name);
        print(f'\nПереименовываем файл:')
        TestApi7.file_move('/' + new_path_dir + '/' + file_name, '/' + new_path_dir + '/' + file_name_rename);

        #TestApi7.dir_delete(new_path_dir)
        #TestApi7.dir_list_discover('/', '')
