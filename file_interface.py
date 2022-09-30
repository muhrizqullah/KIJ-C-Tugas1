import os
import base64
from glob import glob


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

        return dict(status='OK', filename=filename, data=data)

    def post(self, params=[]):
        filename = params[0]
        data = params[1]

        with open(filename, 'xb') as fp:
            fp.write(base64.b64decode(data))

        return dict(status='OK', data=filename)

    def delete(self, params=[]):
        filename = params[0]

        os.remove(filename)

        return dict(status='OK', data=f'{filename} deleted')


if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
