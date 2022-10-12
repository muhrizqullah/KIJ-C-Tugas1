from base64 import b64decode, b64encode
from aes import myAES
from des import myDES
from rc4 import myRC4
from diy_aes import DiyAes
from diy_des import DiyDes

import time

DES_KEY = b'inikunci'
AES_KEY = b'kuncikuadalahini'
RC4_KEY = b'kuncikuadatiga'
DEFAULT_ENCRYPTION = "rc4"

def encrypt(encryption, data, show_output=False):
    encrypted_data = b''
    iv = b''

    start = time.time()

    if (encryption == "aes"):
        aes = myAES(AES_KEY, data)
        encrypted_data, iv = aes.encrypt()

    elif (encryption == "des"):
        des = myDES(DES_KEY, data)
        encrypted_data, iv = des.encrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        encrypted_data = rc4.encrypt()

    elif (encryption == "diy_aes"):
        aes = DiyAes(AES_KEY)
        encrypted_data, iv = aes.encrypt_cbc(data)

    elif (encryption == "diy_des"):
        des = DiyDes(DES_KEY)
        encrypted_data, iv = des.encrypt_cbc(data)

    else:
        raise ValueError("Unknown encryption method")

    elapsed = time.time() - start
    
    if show_output:
        print("Time taken for encryption:", elapsed * 1000, "ms")
        print("Plaintext:", data)
        print("Plaintext Hex:", data.hex())
        print("Ciphertext:", encrypted_data)
        print("Ciphertext Hex:", encrypted_data.hex())

    return encrypted_data, iv

def decrypt(encryption, data, iv, show_output=False):
    decrypted_data = ""
    
    start = time.time()

    if (encryption == "aes"):
        aes = myAES(AES_KEY, data, iv)
        decrypted_data = aes.decrypt()

    elif (encryption == "des"):
        des = myDES(DES_KEY, data, iv)
        decrypted_data = des.decrypt()

    elif (encryption == "rc4"):
        rc4 = myRC4(RC4_KEY, data)
        decrypted_data = rc4.decrypt()

    elif (encryption == "diy_aes"):
        aes = DiyAes(AES_KEY)
        decrypted_data = aes.decrypt_cbc(data, iv)

    elif (encryption == "diy_des"):
        des = DiyDes(DES_KEY)
        decrypted_data, iv = des.decrypt_cbc(data)

    else:
        raise ValueError("Unknown encryption method")

    elapsed = time.time() - start
        
    if show_output:
        print("Time taken for decryption:", elapsed * 1000, "ms")
        print("Ciphertext:", data)
        print("Ciphertext Hex:", data.hex())
        print("Plaintext:", decrypted_data)
        print("Plaintext Hex:", decrypted_data.hex())

    return decrypted_data

if __name__ == '__main__':
    data = b"Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis rem atque magnam vero nostrum ea ipsum similique minus ipsam dolores laudantium, possimus, commodi officiis ab in eaque provident voluptas sunt."

    print("AES")
    encrypted_data, iv = encrypt('aes', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('aes', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)

    print("\nDES")
    encrypted_data, iv = encrypt('des', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('des', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)

    print("\nRC4")
    encrypted_data, iv = encrypt('rc4', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('rc4', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)

    print("\nDIY AES")
    encrypted_data, iv = encrypt('diy_aes', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('diy_aes', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)

    print("\nDIY DES")
    encrypted_data, iv = encrypt('diy_des', data)
    print("Encrypted data: " , encrypted_data)
    print("IV: " , iv)
    decrypted_data = decrypt('diy_des', encrypted_data, iv)
    print("Decrypted data: " , decrypted_data)
