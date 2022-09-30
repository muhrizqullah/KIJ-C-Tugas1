import socket
import json
import base64
import logging
import shlex

SERVER_ADDRESS = ('127.0.0.1', 6666)
BUFFER_SIZE = 4096


def send_command(command_str=""):
    global SERVER_ADDRESS
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
    except:
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


def remote_get(filename=""):
    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"GET {filename}"
    result = send_command(command_str)
    if not remote_error(result):
        new_filename = result['filename']
        data = base64.b64decode(result['data'])
        with open(new_filename, 'wb') as fp:
            fp.write(data)

        print(f"{new_filename} successfully downloaded")
        return True
    else:
        return False


def remote_post(filename=""):
    data = ""

    try:
        with open(filename, 'rb') as fp:
            data = base64.b64encode(fp.read()).decode('utf-8')
    except FileNotFoundError:
        print("Error: file not found")
        return False

    if " " in filename:
        filename = f'"{filename}"'

    command_str = f"POST {filename} {data}"
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
    print("- upload <filename>")
    print("- delete <filename>")

    try:
        while True:
            print("\nEnter command (^C to exit):")
            handle_command(input())
    except KeyboardInterrupt:
        print("\nProgram exited.")