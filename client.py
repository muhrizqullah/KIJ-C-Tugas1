import socket
import json
import base64
import shlex
from encrypt_decrypt import encrypt, decrypt


SERVER_ADDRESS = ('127.0.0.1', 6666)
BUFFER_SIZE = 4096


def send_command(command_str):
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


def remote_get(encryption, filename):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"GET {filename} {encryption}"
    result = send_command(command_str)
    if not remote_error(result):
        new_filename = result['filename']
        
        data = decrypt(encryption, result['data'], result['iv'])
        data = base64.b64decode(data)

        with open(new_filename, 'wb') as fp:
            fp.write(data)

        print(f"{new_filename} successfully downloaded")
        return True
    else:
        return False


def remote_post(encryption, filename):
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


def remote_delete(filename):
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
            remote_get(rest[0], rest[1])
        elif command.lower() == "upload":
            remote_post(rest[0], rest[1])
        elif command.lower() == "delete":
            remote_delete(rest[0])
        else:
            print("Error: unknown command")
    except IndexError:
        print(f"Error: Some parameters are missing")


if __name__ == '__main__':
    print("Command list:")
    print("- list")
    print("- download <encryption> <filename>")
    print("- upload <encryption> <filename>")
    print("- delete <filename>")
    print("\nNote:")
    print("- surround filename with double quotes if it contains spaces")
    print("- encryption can either be 'aes', 'des', 'rc4', or 'diy_aes'")

    try:
        while True:
            print("\nEnter command (^C to exit):")
            handle_command(input())
    except KeyboardInterrupt:
        print("\nProgram exited.")
