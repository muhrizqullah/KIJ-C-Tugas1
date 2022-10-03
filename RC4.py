MODULUS = 256

class RC4:
    
    def initialisation(key):
        key_length = len(key)
        S = []
        T = []
        i = 0
        
        for i in range(MODULUS):
            S.append(i)
            if key_length < 256:
                T.append(key[i % key_length])
        return permutation(S, T)
    
    def permutation(S, T):
        j = 0
        
        for i in range(MODULUS):
            j = (j + S[i] + T[i]) % MODULUS
            S[i], S[j] = S[j], S[i]
            
        return S
    
    def PRNG(S):
        i, j = 0
        
        while True:
            i = (i + 1) % MODULUS
            j = (j + S[i]) % MODULUS
            
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % MOD]
            yield K
    
    def getKeystream(key):
        S = initialisation(key)
        return PRNG(S)
       