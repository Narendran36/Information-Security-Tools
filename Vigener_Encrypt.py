# plaintext and codeword in CAPITAL LETTERS  only

def vigenere_encrypt(plaintext, codeword):
    size = len(plaintext)
    size2 = len(codeword)
    rep = size//size2+1
    if rep!= 0:
        codeword = codeword * rep
    crypto = ""
    for x,y in zip(plaintext,codeword[:size]):
        shift = ord(y) - 65
        z = ord(x) + shift
        if z > 90:
            z = (z - 90) + 64
        crypto += chr(z)
    return crypto
