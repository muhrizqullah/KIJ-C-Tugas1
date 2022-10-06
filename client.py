import socket
import json
import base64
from base64 import b64decode, b64encode
import shlex

from aes import myAES
from des import myDES
from rc4 import myRC4

SERVER_ADDRESS = ('127.0.0.1', 6666)
BUFFER_SIZE = 4096
DES_KEY = b'inikunci'
AES_KEY = b'kuncikuadalahini'
RC4_KEY = b'kuncikuadatiga'
DEFAULT_ENCRYPTION = "des"

def send_command(command_str=""):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(SERVER_ADDRESS)

    command_str += "\r\n\r\n"

    try:
        sock.sendall(command_str.encode())
        data_received = ""
        while True:
            data = sock.recv(BUFFER_SIZE)
            if data:
                data_received += data.decode()
                if "\r\n\r\n" in data_received:
                    break
            else:
                break

        hasil = json.loads(data_received)
        return hasil
    except Exception:
        return False


def encrypt(encryption, data):
    encrypted_data = ""
    data = data.encode()
    print("Encrypting... " , data)

    if (encryption == "aes"):
        aes = myAES(AES_KEY, data.decode())
        encrypted_data,iv = aes.encrypt()
        

    elif (encryption == "des"):
        des = myDES(DES_KEY, data)
        encrypted_data, iv = des.encrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        encrypted_data = rc4.encrypt()

    iv = b64encode(iv).decode()
    encrypted_data = b64encode(encrypted_data).decode()
    return encrypted_data, iv

def decrypt(encryption, data, iv):
    decrypted_data = ""
    iv = b64decode(iv)
    data = b64decode(data)

    if (encryption == "aes"):
        aes = myAES(DES_KEY, data, iv)
        decrypted_data = aes.decrypt()

    elif (encryption == "des"):
        des = myDES(DES_KEY, data, iv)
        decrypted_data = des.decrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        decrypted_data = rc4.decrypt()

    return decrypted_data.decode()


def remote_list():
    command_str = f"LIST"
    result = send_command(command_str)
    if not remote_error(result):
        print("Files: ")
        for filename in result['data']:
            print(f"- {filename}")
        return True
    else:
        return False


def remote_get(filename=""):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"GET {filename}"
    result = send_command(command_str)
    if not remote_error(result):
        new_filename = result['filename']
        
        data = decrypt(DEFAULT_ENCRYPTION, result['data'], result['iv'])
        data = base64.b64decode(data)

        with open(new_filename, 'wb') as fp:
            fp.write(data)

        print(f"{new_filename} successfully downloaded")
        return True
    else:
        return False


def remote_post(encryption, filename=""):
    data = ""

    try:
        with open(filename, 'rb') as fp:
            data = base64.b64encode(fp.read()).decode('utf-8')
    except FileNotFoundError:
        print("Error: file not found")
        return False

    if " " in filename:
        filename = f'"{filename}"'

    data, iv = encrypt(encryption, data)

    command_str = f"POST {filename} {data} {encryption} {iv}"
    result = send_command(command_str)

    if not remote_error(result):
        print("File successfully uploaded")
        return True
    else:
        return False


def remote_delete(filename=""):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"DELETE {filename}"
    result = send_command(command_str)

    if not remote_error(result):
        print("File successfully deleted")
        return True
    else:
        return False


def remote_error(result):
    if (result['status'] == 'OK'):
        return False

    if (result['data']):
        print(f"Error: {result['data']}")

    return True


def handle_command(command):
    command, *rest = shlex.split(command)

    try:
        if command.lower() == "list":
            remote_list()
        elif command.lower() == "download":
            remote_get(rest[0])
        elif command.lower() == "upload":
            remote_post(rest[0])
        elif command.lower() == "delete":
            remote_delete(rest[0])
        else:
            print("Error: unknown command")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    print("Command list:")
    print("- list")
    print("- download <filename>")
    print("- upload <encryption> <filename>")
    print("- delete <filename>")
    print("Note: surround filename with double quotes if it contains spaces")
    print("Note2: encryption can either be 'aes', 'des', or 'rc4'.")

    try:
        while True:
            print("\nEnter command (^C to exit):")
            handle_command(input())
    except KeyboardInterrupt:
        print("\nProgram exited.")
