import os
import base64
from base64 import b64decode, b64encode
from glob import glob
from encrypt_decrypt import encrypt, decrypt

class FileInterface:
    def __init__(self):
        if not os.path.exists("files/"):
            os.mkdir("files/")

        os.chdir('files/')

    def list(self, _params=[]):
        file_list = glob('*.*')
        return dict(status='OK', data=file_list)

    def get(self, params=[]):
        filename = params[0]
        encryption = params[1]

        if (filename == ''):
            return None

        data = ""
        with open(filename, 'rb') as fp:
            data = fp.read()

        data, iv = encrypt(encryption, data)
        data = base64.b64encode(data).decode()
        iv = base64.b64encode(iv).decode()

        return dict(status='OK', filename=filename, data=data, iv=iv)

    def post(self, params=[]):
        filename = params[0]
        data = base64.b64decode(params[1])
        encryption = params[2]
        
        if len(params) > 3:
            iv = base64.b64decode(params[3])
        else:
            iv = b''

        data = decrypt(encryption, data, iv)

        with open(filename, 'xb') as fp:
            fp.write(data)

        return dict(status='OK', data=filename)

    def delete(self, params=[]):
        filename = params[0]

        os.remove(filename)

        return dict(status='OK', data=f'{filename} deleted')


if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
