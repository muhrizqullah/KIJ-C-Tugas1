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
    byte = str.encode()
    print("\nplaintext: \n", byte)

    des = myDES(key, byte)
    enc, iv = des.encrypt()
    print("\niv: \n", iv)
    print("\nciphertext: \n", enc)

    des2 = myDES(key, enc, iv)
    dec = des2.decrypt()
    print("\ndecrypted:\n", dec)