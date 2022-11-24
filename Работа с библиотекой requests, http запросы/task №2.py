import requests
from Yand import TOKEN


class YaUploader:
    base_host = 'https://cloud-api.yandex.net'
    def __init__(self, token: str):
        self.token = token


    def upload(self, file_path: str):
        heders = {'Authorization': f'OAuth {TOKEN}'}
        params = {'path': file_path, 'overwrite': True}
        uri = '/v1/disk/resources/upload'
        request_url = self.base_host + uri
        response = requests.get(request_url, headers=heders, params=params)
        link = response.json()['href']
        response_upload = requests.put(link, data=open(file_path, 'rb'), headers=heders)


if __name__ == '__main__':
    path_to_file = 'Test.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

