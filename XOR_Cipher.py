def encrypt(plaintext, k):
    return "".join([chr(ord(a)^ord(b)) for a,b in zip(plaintext,k)])
