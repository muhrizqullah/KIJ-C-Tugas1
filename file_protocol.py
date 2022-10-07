import json
import re

from file_interface import FileInterface


class FileProtocol:
    def __init__(self):
        self.file = FileInterface()

    def proses_string(self, data=''):
        c = [''.join(t) for t in re.findall(
            r"""([^\s"']+)|"([^"]*)"|'([^']*)'""", data)]

        try:
            c_request = c[0].strip()
            params = [x for x in c[1:]]

            cl = getattr(self.file, c_request.lower())(params)

            return json.dumps(cl)
        except AttributeError:
            return json.dumps(dict(status='ERROR', data='invalid request'))
        except IndexError:
            return json.dumps(dict(status='ERROR', data='some parameters are missing'))
        except FileExistsError:
            return json.dumps(dict(status='ERROR', data='filename already exists on server'))
        except FileNotFoundError:
            return json.dumps(dict(status='ERROR', data='file not found on server'))
        except ValueError:
            return json.dumps(dict(status='ERROR', data='wrong parameter(s)'))
        except Exception as e:
            return json.dumps(dict(status='ERROR', data=str(e)))


if __name__ == '__main__':
    fp = FileProtocol()
    print(fp.proses_string("LIST"))
    print(fp.proses_string("GET pokijan.jpg"))
