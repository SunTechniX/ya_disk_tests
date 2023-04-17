#import requests
#import json
from .base_api import BaseApi
from .locators import BaseApiLocators

class TestApi_01(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = BaseApiLocators.URL
        self.url_files = BaseApiLocators.URLfiles
        self.token = BaseApiLocators.TOKEN
        self.headers = BaseApiLocators.HEADERS

    def test_list_files(self):
        print()
        self.list_files('')

    def test_obj_exist(self, path):
        self.object_exist(path)

    def test_list_dirs(self):
        self.list_dirs_discover('/', '')

    def test_create_dir(self, path):
        self.create_dir(path)

    def test_delete_dir(self, path):
        self.delete_dir(path)
