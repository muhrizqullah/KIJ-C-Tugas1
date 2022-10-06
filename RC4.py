from base64 import b64decode, b64encode
from Crypto.Cipher import ARC4


class myRC4:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.cipher = ARC4.new(self.key)
    
    def encrypt(self):
        encrypted_data = self.cipher.encrypt(self.data)
        return encrypted_data
    
    def decrypt(self):
        decrypted_data = self.cipher.decrypt(self.data)
        return decrypted_data

if __name__ == '__main__':

    key = b'akbars key'

    str = "halo dunia apa kabar"
    print("str: ", str)

    byte = str.encode()
    print("byte: ", byte)

    rc4 = myRC4(key, byte)
    enc= rc4.encrypt()
    print("enc: ", enc)

    b64sen = b64encode(enc).decode()
    print("b64sent: ", b64sen)

    byterec = b64decode(b64sen)
    print("byterec = enc: ", byterec)

    rc42 = myRC4(key, byterec)
    dec = rc42.decrypt()
    print("dec = byte: ", dec)

    b64 = dec.decode()
    print(b64)