from base64 import b64decode, b64encode
from pydoc import plain
import Crypto
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class myDES:
    def __init__(self, key, data, iv = None, mode = DES.MODE_CBC):
        self.key = key
        self.mode = mode
        self.data = data
        self.cipher = DES.new(self.key, self.mode, iv)
    
    def encrypt(self):
        encrypted_data = self.cipher.encrypt(pad(self.data, 8))
        return encrypted_data, self.cipher.iv

    def decrypt(self):
        decrypted_data = unpad(self.cipher.decrypt(self.data), 8)
        return decrypted_data

if __name__ == '__main__':

    key = b'-8B key-'

    str = "halo dunia apa kabar"
    print("str: ", str)

    byte = str.encode()
    print("byte: ", byte)

    des = myDES(key, byte)
    enc, iv = des.encrypt()
    print("iv: ", iv)
    print("enc: ", enc)

    b64sen = b64encode(enc).decode()
    print("b64sent: ", b64sen)

    byterec = b64decode(b64sen)
    print("byterec = enc: ", byterec)

    des2 = myDES(key, byterec, iv)
    dec = des2.decrypt()
    print("dec = byte: ", dec)

    b64 = dec.decode()
    print(b64)