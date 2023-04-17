class BaseApiLocators():
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    URLfiles = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    TOKEN = 'y0_AgAAAABo4rs8AADLWwAAAADfTfoKq18EkRInRwq_fJlOcVgsdIMkdBw'
    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    fields = '_embedded.items.name,_embedded.items.type'
    FILE_FOR_COPY = 'Файл для копирования.docx'
    FILE_FOR_UPLOAD = 'Файл для загрузки.txt'

