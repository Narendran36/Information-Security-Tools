from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, k):
    pass # return iv + ciphertext (in bytes)
    iv = Random.get_random_bytes(16)
    ciphertext = iv
    cipher = AES.new(k,AES.MODE_CBC,iv)
    etext = cipher.encrypt(plaintext)
    ciphertext += etext
    return ciphertext

def aes_decrypt(ciphertext, k):
    pass # return plaintext (in 'latin1')
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(k,AES.MODE_CBC,iv)
    msg = cipher.decrypt(ciphertext)
    return msg.decode('latin1')
