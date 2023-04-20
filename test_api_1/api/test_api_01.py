from .base_api import BaseApi
from .locators import BaseApiLocators

class TestApi_01(BaseApi):
    def __init__(self):
        super().__init__()
        self.token = BaseApiLocators.TOKEN
        self.headers = BaseApiLocators.HEADERS

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
        response = self.request_put(req_path)
        self.msg_response_code(response, path)
        assert response.status_code == 201, "Directory not created!"


    def dir_delete(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}&permanently=true'
        response = self.request_delete(req_path)
        self.msg_response_code(response, path, 'dir')
        assert response.status_code == 202 or response.status_code == 204, "Object not Deleted!"


    def dir_list_discover(self, path, show_tree):
        req_path = f'{BaseApiLocators.URL}?path={path}'
        response = self.request_get(req_path)
        json_response = response.json()
        assert self.JSON_check(json_response), "JSON Error! - Maybe Wrong format!"

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
        response = self.request_get(req_path)
        json_response = response.json()
        #print(json_response)
        assert self.JSON_check(json_response), "JSON Error! - Maybe Wrong format!"

        for key, value in json_response.items():
            if type(value) == list:
                print(f'{key}:')
                for line in value:
                    print(line['type'], line['name'])

    def object_exist(self, path):
        req_path = f'{BaseApiLocators.URL}?path={path}&limit=1'
        response = self.request_get(req_path)
        self.msg_response_code(response, path)
        assert response.status_code == 200, "Object not exist!"

    def file_copy(self, path_from, path_to):
        req_path = f'{BaseApiLocators.URLcopy}?from={path_from}&path={path_to}&overwrite=true'
        response = self.request_post(req_path)
        self.msg_response_code(response, path_to)
        assert response.status_code == 201 or response.status_code == 202, "Object not Copyed!"

    def file_move(self, path_from, path_to):
        req_path = f'{BaseApiLocators.URLmove}?from={path_from}&path={path_to}&overwrite=true'
        response = self.request_post(req_path)
        self.msg_response_code(response, path_to)
        assert response.status_code == 201 or response.status_code == 202, "Error on move object!"