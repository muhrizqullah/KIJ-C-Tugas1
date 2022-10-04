import os
import base64
from base64 import b64decode, b64encode
from glob import glob
from client import encrypt
from des import myDES

DES_KEY = b'inikunci'
DEFAULT_ENCRYPTION = "des"

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
        if (filename == ''):
            return None

        data = ""
        with open(filename, 'rb') as fp:
            data = base64.b64encode(fp.read()).decode()

        data, iv = encrypt(DEFAULT_ENCRYPTION, data)

        return dict(status='OK', filename=filename, data=data, iv=iv)

    def post(self, params=[]):
        filename = params[0]
        data = params[1]
        encryption = params[2]
        iv = params[3]

        data = self.decrypt(encryption, data, iv)

        with open(filename, 'xb') as fp:
            fp.write(base64.b64decode(data))

        return dict(status='OK', data=filename)

    def delete(self, params=[]):
        filename = params[0]

        os.remove(filename)

        return dict(status='OK', data=f'{filename} deleted')

    def encrypt(self, encryption, data):
        encrypted_data = ""
        data = data.encode()
        print("Encrypting... " , data)

        if (encryption == "aes"):
            # enc = aes(key, data)
            # encrypted_data = aes.encrypt
            TODO

        elif (encryption == "des"):
            des = myDES(DES_KEY, data)
            encrypted_data, iv = des.encrypt()

        elif (encryption == "rc4"):
            # rc4 = RC4
            TODO

        iv = b64encode(iv).decode()
        encrypted_data = b64encode(encrypted_data).decode()
        return encrypted_data, iv

    def decrypt(self, encryption, data, iv):
        decrypted_data = ""
        iv = b64decode(iv)
        data = b64decode(data)

        if (encryption == "aes"):
            # enc = aes(key, data)
            # encrypted_data = aes.decrypt
            TODO

        elif (encryption == "des"):
            des = myDES(DES_KEY, data, iv)
            decrypted_data = des.decrypt()

        elif (encryption == "rc4"):
            # rc4 = RC4
            TODO

        return decrypted_data.decode()


if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
