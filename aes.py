from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode,b64decode
import json

class myAES:
    def __init__(self,key,data, iv = None, mode = AES.MODE_CBC):
       self.key=key
       self.data=data
       self.e_cipher = AES.new(self.key,mode,iv)
       self.iv=iv

    def encrypt(self):
        chipertext = self.e_cipher.encrypt(pad(self.data, AES.block_size))
        return chipertext,self.e_cipher.iv
    
    def decrypt(self):
        pt = unpad(self.e_cipher.decrypt(self.data), AES.block_size)
        return pt

if __name__ == '__main__':
    key = get_random_bytes(16)
    data = b'hello from other side hallo hi'
    aes=myAES(key,data)
    chipertext,iv=aes.encrypt()
    iv = b64encode(iv).decode('utf-8')
    chipertext = b64encode(chipertext).decode('utf-8')
    aes=myAES(key,b64decode(chipertext),b64decode(iv))
    plaintext=aes.decrypt()
    print(plaintext)

    
