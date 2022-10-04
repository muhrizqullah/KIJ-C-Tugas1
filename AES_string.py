from Crypto.Cipher import AES

class myAES:
    def __init__(self,key,data):
       self.key=key
       self.data=data
       self.e_cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self):
        e_data = self.e_cipher.encrypt(self.data)
        print("Encryption was: ", e_data)
        return e_data
    
    def decrypt(self,e_data):
        d_cipher = AES.new(self.key, AES.MODE_EAX, self.e_cipher.nonce)
        d_data = d_cipher.decrypt(e_data)
        print("Original Message was: ", d_data)

if __name__ == '__main__':
    key = b'Sixteen byte key'
    data = b'hello from other side hallo hi'
    aes=myAES(key,data)
    aes.decrypt(aes.encrypt())