from base64 import b64decode, b64encode
from aes import myAES
from des import myDES
from rc4 import myRC4

DES_KEY = b'inikunci'
AES_KEY = b'kuncikuadalahini'
RC4_KEY = b'kuncikuadatiga'
DEFAULT_ENCRYPTION = "rc4"

def encrypt(encryption, data):
    encrypted_data = ""
    iv = b''
    data = data.encode()
    print("Encrypting... " , data)

    if (encryption == "aes"):
        aes = myAES(AES_KEY, data)
        encrypted_data, iv = aes.encrypt()

    elif (encryption == "des"):
        des = myDES(DES_KEY, data)
        encrypted_data, iv = des.encrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        encrypted_data = rc4.encrypt()

    else:
        raise ValueError("Unknown encryption method")

    iv = b64encode(iv).decode()
    encrypted_data = b64encode(encrypted_data).decode()
    return encrypted_data, iv

def decrypt(encryption, data, iv):
    decrypted_data = ""
    iv = b64decode(iv)
    data = b64decode(data)
    print("Decrypting... " , data)

    if (encryption == "aes"):
        aes = myAES(AES_KEY, data, iv)
        decrypted_data = aes.decrypt()

    elif (encryption == "des"):
        des = myDES(DES_KEY, data, iv)
        decrypted_data = des.decrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        decrypted_data = rc4.decrypt()

    else:
        raise ValueError("Unknown encryption method")

    return decrypted_data.decode()

if __name__ == '__main__':
    data = "hello from other side"
    encrypted_data, iv = encrypt('aes', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('aes', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)
