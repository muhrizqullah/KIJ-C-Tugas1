import random

PC1_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12,  4
]

PC2_TABLE = [
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INVERSE_TABLE = [
    40, 8,  48, 16, 56, 24, 64, 32,
    39, 7,  47, 15, 55, 23, 63, 31,
    38, 6,  46, 14, 54, 22, 62, 30,
    37, 5,  45, 13, 53, 21, 61, 29,
    36, 4,  44, 12, 52, 20, 60, 28,
    35, 3,  43, 11, 51, 19, 59, 27,
    34, 2,  42, 10, 50, 18, 58, 26,
    33, 1,  41, 9,  49, 17, 57, 25
]

E_TABLE = [
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

SBOX_TABLE = [
    [
        14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7,
        0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8,
        4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0,
        15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13
    ],
    [
        15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10,
        3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5,
        0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15,
        13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9
    ],
    [
        10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8,
        13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1,
        13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7,
        1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12
    ],
    [
        7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15,
        13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9,
        10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4,
        3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14
    ],
    [
        2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9,
        14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6,
        4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14,
        11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3
    ],
    [
        12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11,
        10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8,
        9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6,
        4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13
    ],
    [
        4,  11, 2,  14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1,
        13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6,
        1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2,
        6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12
    ],
    [
        13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7,
        1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2,
        7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8,
        2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11
    ]
]

PBOX_TABLE = [
    16, 7,  20, 21,
    29, 12, 28, 17,
    1,  15, 23, 26,
    5,  18, 31, 10,
    2,  8,  24, 14,
    32, 27, 3,  9,
    19, 13, 30, 6,
    22, 11, 4,  25
]

class DiyDes(object):
    def __init__(self, key):
        if type(key) != bytes:
            raise TypeError("key must be bytes")

        if len(key) != 8:
            raise ValueError('Key must be 8 bytes long')

        self.key = self.__bytes_to_bits(key)
        self.subkeys = [0] * 16
        self.__generate_internal_key()

    def __bits_to_bytes(self, input):
        output = []
        for i in range(0, len(input), 8):
            output.append(int(''.join([str(j) for j in input[i:i+8]]), 2))

        return bytes(output)

    def __bytes_to_bits(self, input):
        output = []
        for i in input:
            output += [int(j) for j in bin(i)[2:].zfill(8)]

        return output

    def __left_shift(self, input, n):
        return input[n:] + input[:n]

    def __generate_internal_key(self):
        key = [0] * 56
        for i in range(56):
            key[i] = self.key[PC1_TABLE[i] - 1]
            
        left = key[:28]
        right = key[28:]

        for i in range(16):
            if i == 0 or i == 1 or i == 8 or i == 15:
                left = self.__left_shift(left, 1)
                right = self.__left_shift(right, 1)

            else:
                left = self.__left_shift(left, 2)
                right = self.__left_shift(right, 2)

            temp = left + right
            internal_key = [0] * 48
            for j in range(48):
                internal_key[j] = temp[PC2_TABLE[j] - 1]
            
            self.subkeys[i] = internal_key

    def __initial_permutation(self, input):
        output = [0] * 64
        for i in range(64):
            output[i] = input[IP_TABLE[i] - 1]

        return output

    def __final_permutation(self, input):
        output = [0] * 64
        for i in range(64):
            output[i] = input[IP_INVERSE_TABLE[i] - 1]

        return output

    def __expansion_permutation(self, input):
        output = [0] * 48
        for i in range(48):
            output[i] = input[E_TABLE[i] - 1]

        return output

    def __xor(self, a, b):
        return [i ^ j for i, j in zip(a, b)]

    def __xor_bytes(self, a, b):
        return [a[i] ^ b[i] for i in range(len(a))]

    def __sbox(self, input):
        output = [0] * 32
        for i in range(8):
            row = input[i * 6] * 2 + input[i * 6 + 5]
            col = input[i * 6 + 1] * 8 + input[i * 6 + 2] * 4 + input[i * 6 + 3] * 2 + input[i * 6 + 4]
            val = SBOX_TABLE[i][row * 16 + col]
            output[i * 4] = (val & 8) >> 3
            output[i * 4 + 1] = (val & 4) >> 2
            output[i * 4 + 2] = (val & 2) >> 1
            output[i * 4 + 3] = val & 1

        return output

    def __pbox(self, input):
        output = [0] * 32
        for i in range(32):
            output[i] = input[PBOX_TABLE[i] - 1]

        return output

    def __f(self, input, key):
        right = self.__expansion_permutation(input)
        right = self.__xor(right, key)
        right = self.__sbox(right)
        right = self.__pbox(right)

        return right

    def __encipher(self, input):
        left = input[:32]
        right = input[32:]

        for i in range(16):
            temp = right
            right = self.__xor(self.__f(right, self.subkeys[i]), left)
            left = temp

        return right + left

    def __decipher(self, input):
        left = input[:32]
        right = input[32:]

        for i in range(15, -1, -1):
            temp = right
            right = self.__xor(self.__f(right, self.subkeys[i]), left)
            left = temp

        return right + left
    
    def __encrypt_block(self, input):
        input = self.__initial_permutation(input)
        output = self.__encipher(input)
        output = self.__final_permutation(output)

        return output

    def __decrypt_block(self, input):
        input = self.__initial_permutation(input)
        output = self.__decipher(input)
        output = self.__final_permutation(output)

        return output

    # PKCS#7 padding
    # ref: https://stackoverflow.com/a/54166852/18277301
    def __pad(self, data):
        pad_len = 8 - len(data) % 8

        return data + bytes([pad_len] * pad_len)

    def __unpad(self, data):
        pad_len = data[-1]

        return data[:-pad_len]

    def __split_blocks(self, data):
        return [data[i:i+8] for i in range(0, len(data), 8)]

    def encrypt_cbc(self, data):
        data = self.__pad(data)
        
        plaintext = self.__split_blocks(data)
        iv = random.randbytes(16)
        # iv = b'O\x9b\x8bq\x97\x1e\x83\xda'
        ciphertext = bytearray()
        previous = iv

        for i in plaintext:
            temp = bytes(self.__xor_bytes(i, previous))
            temp = self.__bits_to_bytes(self.__encrypt_block(self.__bytes_to_bits(temp)))
            ciphertext.extend(temp)

            previous = temp

        return bytes(ciphertext), iv

    def decrypt_cbc(self, data, iv):
        ciphertext = self.__split_blocks(data)
        plaintext = bytearray()
        previous = iv

        for i in ciphertext:
            temp = self.__bits_to_bytes(self.__decrypt_block(self.__bytes_to_bits(i)))
            temp = bytes(self.__xor_bytes(temp, previous))
            plaintext.extend(temp)
            previous = i

        return self.__unpad(bytes(plaintext))
        
if __name__ == '__main__':
    key = b'-8B sey-'
    des = DiyDes(key)

    data = b"halo dunia apa kabar"

    ciphertext, iv = des.encrypt_cbc(data)
    print("plaintext:\n", data)
    print("\nciphertext:\n", ciphertext)
    print("\niv:\n", iv)
    print("\ndecrypted:\n", des.decrypt_cbc(ciphertext, iv))