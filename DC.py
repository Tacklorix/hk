import os
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl

# اطلاعات ربات تلگرام
BOT_TOKEN = '7697849074:AAFGwzJ9NNW74pSEJ2Y257AJYTtI_-tOdD8'
CHAT_ID = '7092240057'
FILE_PATH = 'DC.zip'
CHUNK_SIZE = 45 * 1024 * 1024

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT@SECLEVEL=1')
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount('https://', SSLAdapter())

def split_file(file_path, chunk_size):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    num_chunks = (file_size + chunk_size - 1) // chunk_size

    with open(file_path, 'rb') as f:
        for i in range(num_chunks):
            chunk = f.read(chunk_size)
            chunk_file_name = f'{file_name}.part{i+1:03d}'
            chunk_file_path = os.path.join(os.path.dirname(file_path), chunk_file_name)

            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(chunk)

            yield chunk_file_path

def send_chunk(chat_id, file_path):
    try:
        with open(file_path, 'rb') as f:
            response = session.post(
                f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument',
                files={'document': f},
                data={'chat_id': chat_id}
            )
            if response.status_code == 200:
                print(f' {file_path}')
            else:
                print(f'{file_path}: {response.text}')
    except Exception as e:
        print(f'{file_path}: {e}')

def main():
    if not os.path.exists(FILE_PATH):
        print("")
        return

    for chunk_file_path in split_file(FILE_PATH, CHUNK_SIZE):
        send_chunk(CHAT_ID, chunk_file_path)
        os.remove(chunk_file_path)
        time.sleep(2)

if __name__ == '__main__':
    main()