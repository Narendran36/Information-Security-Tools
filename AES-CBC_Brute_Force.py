from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english # previously defined functions

def brute_force_aes(ciphertext):
    print(ciphertext)
    # return plaintext (in 'latin1', from aes_decrypt()), k
    for i in range(999999):
        k = "036"+str(i).zfill(6)+"0000000"
        msg = aes_decrypt(ciphertext,k)
        if is_english(msg):
            return msg, k.encode()
    return -1
