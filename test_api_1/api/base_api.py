import requests
from requests import Response
from .locators import BaseApiLocators

class BaseApi:
    def __init__(self):
        self.token = None
        self.headers = None
        self.user_id = None
        self.body = None

    def post_request(self, url: str, **kwargs: dict) -> Response:
        return requests.post(url, timeout=TIMEOUT_ACCIDENTAL,
                             headers={'Autorization': f'Bearer {self.token}'}, **kwargs)

    def msg_response_code(self, response, path, obj='obj'):
        if response.status_code == 200:
            print(f'\nОбъект "{path}" существует!')
        elif response.status_code == 201:  # 201 Created
            print(f'\nОбъект "{path}" успешно создан/скопирован!')
        elif response.status_code == 202:  # Accepted
            if obj == 'obj':
                print(f'\nКопирование объекта "{path}" начато!')
            elif obj == 'dir':
                print(f'\nНепустой каталог "{path}" поставлен в очуредь на удаление!')
        elif response.status_code == 204:
            if obj == 'obj':
                print(f'\nОбъект "{path}" успешно удалён!') # not check
            elif obj == 'dir':
                print(f'\nПустой каталог "{path}" успешно удалён!')
        elif response.status_code == 404:
            print(f'\nОбъект "{path}" не найден!')
        elif response.status_code == 405:
            print('Метод не поддерживается.')
        elif response.status_code == 409:
            print(f'\nПо пути "{path}" уже существует объект с таким же именем!')
        else:
            json_response = response.json()
            print(path, response, json_response)

    """ Создание каталога. path - Путь к создаваемой папке."""
    def dir_create(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}'
        response = requests.put(req_path, headers=self.headers)
        self.msg_response_code(response, path)


    def dir_delete(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}&permanently=true'
        response = requests.delete(req_path, headers=self.headers)
        self.msg_response_code(response, path, 'dir')


    def dir_list_discover(self, path, show_tree):
        req_path = f'{BaseApiLocators.URL}?path={path}'
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
                                        show_tree = '  ' * (len(show_tree) // 2) + '└─'
                                    self.dir_list_discover(item['path'], show_tree)
                                    if show_tree[0:2] == '  ':
                                        show_tree = show_tree[2:]

    def files_list(self, path):
        req_path = f'{BaseApiLocators.URLfiles}?path={path}'
        response = requests.get(req_path, headers=self.headers)

        json_response = response.json()
        #print(json_response)

        for key, value in json_response.items():
            if type(value) == list:
                print(f'{key}:')
                for line in value:
                    print(line['type'], line['name'])

    def object_exist(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}&limit=1'
        response = requests.get(req_path, headers=self.headers)
        self.msg_response_code(response, path)

    def file_copy(self, path_from, path_to):
        req_path = f'{BaseApiLocators.URLcopy}?from={path_from}&path={path_to}&overwrite=true'
        response = requests.post(req_path, headers=self.headers)
        self.msg_response_code(response, path_to)

    def file_move(self, path_from, path_to):
        req_path = f'{BaseApiLocators.URLmove}?from={path_from}&path={path_to}&overwrite=true'
        response = requests.post(req_path, headers=self.headers)
        self.msg_response_code(response, path_to)
