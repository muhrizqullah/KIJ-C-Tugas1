from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode,b64decode
import json

class myAES:
    def __init__(self,key,data):
       self.key=key
       self.data=data
       self.e_cipher = AES.new(self.key, AES.MODE_CBC)
       self.iv=None

    def encrypt(self):
        e_data = self.e_cipher.encrypt(pad(self.data, AES.block_size))
        iv = b64encode(self.e_cipher.iv).decode('utf-8')
        ct = b64encode(e_data).decode('utf-8')
        result = json.dumps({'iv':iv, 'ciphertext':ct})
        print(result)
        return result
    
    def decrypt(self,json_input):
        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)

if __name__ == '__main__':
    key = get_random_bytes(16)
    data = b'hello from other side hallo hi'
    aes=myAES(key,data)
    aes_encrypt=aes.encrypt()
    aes.decrypt(aes_encrypt)
