#import requests
#import json
from .base_api import BaseApi
from .locators import BaseApiLocators

class TestApi_01(BaseApi):
    def __init__(self):
        super().__init__()
        self.token = BaseApiLocators.TOKEN
        self.headers = BaseApiLocators.HEADERS

    def test_files_list(self):
        print()
        self.files_list('')

    def test_obj_exist(self, path):
        self.object_exist(path)

    def test_dirs_list(self):
        self.dir_list_discover('/', '')

    def test_dir_create(self, path):
        self.dir_create(path)

    def test_dir_delete(self, path):
        self.dir_delete(path)
