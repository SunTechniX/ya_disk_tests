import json
import requests
from requests import Response

class BaseApi:
    def __init__(self):
        self.token = None
        self.headers = None
        self.user_id = None
        self.body = None

    def request_get(self, url: str, **kwargs: dict) -> Response:
        return requests.get(url, headers=self.headers, **kwargs)

    def request_post(self, url: str, **kwargs: dict) -> Response:
        return requests.post(url, headers=self.headers, **kwargs)

    def request_put(self, url: str, **kwargs: dict) -> Response:
        return requests.put(url, headers=self.headers, **kwargs)

    def request_delete(self, url: str, **kwargs: dict) -> Response:
        return requests.delete(url, headers=self.headers, **kwargs)

    def JSON_check(self, json_data):
        try:
            json.loads(str(json_data).replace("'", '"'))
        except ValueError as err:
            return False
        return True
