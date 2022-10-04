from pydoc import plain
import Crypto
from Crypto.Cipher import DES

class myDES:
    def __init__(self, key, mode = DES.MODE_CBC):
        self.key = key
        self.mode = mode
        self.cipher = DES.new(self.key, self.mode)

    def pad(data):
        n = len(data) % 8
        if (n == 0): return data
        return data + (b' ' * (8 - n))
    
    def encrypt(self, data):
        encrypted_data = self.cipher.encrypt(pad(data))
        return encrypted_data

    def decrypt(self, data):
        decrypted_data = self.cipher.decrypt(data)
        return decrypted_data