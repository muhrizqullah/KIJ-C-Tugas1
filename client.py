import socket
import json
import base64
import shlex
from encrypt_decrypt import encrypt, decrypt
import sys

SERVER_ADDRESS = ('127.0.0.1', 6666)
BUFFER_SIZE = 4096


def send_command(command_str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(SERVER_ADDRESS)

    command_str += "\r\n\r\n"
    
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


def remote_list():
    command_str = f"LIST"
    result = send_command(command_str)
    if not remote_error(result):
        print("Files: ")
        for filename in result['data']:
            print(f"- {filename}")


def remote_get(encryption, filename):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"GET {filename} {encryption}"
    result = send_command(command_str)
    if not remote_error(result):
        new_filename = result['filename']
        
        data = base64.b64decode(result['data'])
        iv = base64.b64decode(result['iv'])
        
        data = decrypt(encryption, data, iv, True)

        with open(new_filename, 'wb') as fp:
            fp.write(data)

        print(f"{new_filename} successfully downloaded")


def remote_post(encryption, filename):
    data = ""
    try:
        with open(filename, 'rb') as fp:
            data = fp.read()
    except FileNotFoundError:
        print("Error: file not found")
        return

    if " " in filename:
        filename = f'"{filename}"'

    data, iv = encrypt(encryption, data, True)
    data = base64.b64encode(data).decode()
    iv = base64.b64encode(iv).decode()

    command_str = f"POST {filename} {data} {encryption} {iv}"
    result = send_command(command_str)

    if not remote_error(result):
        print("File successfully uploaded")


def remote_delete(filename):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"DELETE {filename}"
    result = send_command(command_str)

    if not remote_error(result):
        print("File successfully deleted")


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
    except Exception as e:
        print(f"Error: {e}")

def interactive():
    print("Command list:")
    print("- list")
    print("- download <encryption> <filename>")
    print("- upload <encryption> <filename>")
    print("- delete <filename>")
    print("\nNotes:")
    print("- surround filename with double quotes if it contains spaces, e.g. \"file name.txt\"")
    print("- encryption can either be 'aes', 'des', 'rc4', or 'diy_aes'")
    print("- you can also send a single command as an argument to this program, e.g. 'python3 client.py upload aes \"file name.txt\"'")

    try:
        while True:
            print("\nEnter command (^C to exit):")
            handle_command(input())
    except (KeyboardInterrupt):
        print("\nProgram exited.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = " ".join([arg if " " not in arg else f'"{arg}"' for arg in sys.argv[1:]])
        handle_command(command)
    else:
        interactive()
