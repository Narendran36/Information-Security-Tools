import random
import hashlib
import os
from Crypto.Cipher import AES
from Crypto import Random

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.a = random.randint(1,p)

    def publish(self):
        return (g**(self.a))%p

    def encrypt(self, gb, text):
        s = (gb**(self.a))%p
        #s = bytes(s)
        k = hashlib.sha256(str(s).encode()).digest()[:16]
        iv = Random.get_random_bytes(16)
        ciphertext = iv
        cipher = AES.new(k,AES.MODE_CBC,iv)
        #print(text)
        etext = cipher.encrypt(text)
        #print(etext)
        ciphertext += etext
        #print(ciphertext)
        
        #iv = ciphertext[:16]
        #ciphertext = ciphertext[16:]
        #cipher = AES.new(k,AES.MODE_CBC,iv)
        #msg = cipher.decrypt(ciphertext)
        #print(msg)
        #print(msg.decode('latin1'))
        
        return ciphertext
