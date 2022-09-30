import logging
import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        if not os.path.exists("files/"):
            os.mkdir("files/")

        os.chdir('files/')

    def list(self, params=[]):
        try:
            file_list = glob('*.*')
            return dict(status='OK', data=file_list)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None

            data = ""
            with open(filename, 'rb') as fp:
                data = base64.b64encode(fp.read()).decode()

            return dict(status='OK', filename=filename, data=data)
        except FileNotFoundError:
            return dict(status='ERROR', data='file not found')
        except IndexError:
            return dict(status='ERROR', data='no filename specified')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def post(self, params=[]):
        try:
            filename = params[0]
            data = params[1]

            with open(filename, 'xb') as fp:
                fp.write(base64.b64decode(data))

            return dict(status='OK', data=filename)
        except IndexError:
            return dict(status='ERROR', data='some parameters are missing')
        except FileExistsError:
            return dict(status='ERROR', data='filename already exists on server')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def delete(self, params=[]):
        try:
            filename = params[0]

            os.remove(filename)

            return dict(status='OK', data=f'{filename} deleted')
        except IndexError:
            return dict(status='ERROR', data='some parameters are missing')
        except FileNotFoundError:
            return dict(status='ERROR', data='file not found')
        except Exception as e:
            return dict(status='ERROR', data=str(e))


if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
