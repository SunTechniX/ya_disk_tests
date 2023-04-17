import requests
from requests import Response

class BaseApi:
    def __init__(self):
        self.url = None
        self.url_files = None
        self.token = None
        self.headers = None
        self.user_id = None
        self.body = None

    def post_request(self, url: str, **kwargs: dict) -> Response:
        return requests.post(url, timeout=TIMEOUT_ACCIDENTAL,
                             headers={'Autorization': f'Bearer {self.token}'}, **kwargs)

    """ Создание каталога. path - Путь к создаваемой папке."""
    def create_dir(self, path):
        req_path = f'{self.url}?path={path}'
        response = requests.put(req_path, headers=self.headers)
        if response.status_code == 201:
            print(f'\nКаталог "{path}" успешно создан!')
        elif response.status_code == 409:
            print(f'\nПо пути "{path}" уже существует объект с таким же именем!')
        else:
            print(response, response.status_code)

    def delete_dir(self, path):
        req_path = f'{self.url}?path={path}&permanently=true'
        response = requests.delete(req_path, headers=self.headers)
        if response.status_code == 204:
            print(f'\nПустой каталог "{path}" успешно удалён!')
        elif response.status_code == 202:
            print(f'\nНепустой каталог "{path}" поставлен в очуредь на удаление!')
        else:
            print(response, response.status_code)

    def list_dirs_discover(self, path, show_tree):
        req_path = f'{self.url}?path={path}'
        response = requests.get(req_path, headers=self.headers)
        json_response = response.json()

        for key, value in json_response.items():
            if key == '_embedded':
                if type(value) == dict:
                    _items = value.get('items')
                    if _items != None:
                        if len(_items) > 0:
                            for item in _items:
                                itype = item['type']
                                if itype == 'dir':
                                    print(itype, show_tree + item['name'])
                                    if show_tree == '':
                                        show_tree += '└─'
                                    else:
                                        show_tree = ' ' * len(show_tree) + '└─'
                                    self.list_dirs_discover(item['path'], show_tree)

    def list_files(self, path):
        req_path = f'{self.url_files}?path={path}'
        response = requests.get(req_path, headers=self.headers)

        json_response = response.json()
        #print(json_response)

        for key, value in json_response.items():
            if type(value) == list:
                print(f'{key}:')
                for line in value:
                    print(line['type'], line['name'])

    def object_exist(self, path):
        req_path = f'{self.url}?path={path}&limit=1'
        response = requests.get(req_path, headers=self.headers)
        if response.status_code == 200:
            print(f'\nОбъект "{path}" существует!')
        elif response.status_code == 404:
            print(f'\nОбъект "{path}" не найден!')
        else:
            json_response = response.json()
            print(path, response, json_response)

    def copy_file(self, path_from, path_to):
        req_path = f'{self.url}?from={path_from}&path={path_to}&overwrite=true'
        response = requests.put(req_path, headers=self.headers)
        if response.status_code == 201: # 201 Created
            print(f'\nФайл "{path_to}" успешно скопирован!')
        elif response.status_code == 202: # Accepted
            print(f'\nКопирование объекта "{path_to}" начато!')
        elif response.status_code == 409:
            print(f'\nПо пути "{path_to}" уже существует объект с таким же именем!')
        else:
            json_response = response.json()
            print(path_to, response, json_response)