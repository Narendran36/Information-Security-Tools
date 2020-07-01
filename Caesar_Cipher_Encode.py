alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    ciphertext = ""
    for i in plaintext:
        if i not in alphabet:
            ciphertext += i
        else:
            ciphertext += alphabet[(alphabet.index(i)+k)%26]

    return ciphertext


takein = input().split()
plaintext = takein[0]
k = int(takein[1])
print(encrypt(plaintext, k))
