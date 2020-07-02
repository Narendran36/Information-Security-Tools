def get_prg(plaintext_size, k):
    i = 0
    j = 0
    size = len(k)
    k = list(k)
    keystream = ""
    for z in range(0,plaintext_size):
        i = (i + 1)%size
        j = (j + ord(k[i]))%size
        temp = k[i]
        k[i] = k[j]
        k[j] = temp
        key_pos = (ord(k[i])+ord(k[j]))%size
        keystream = keystream + k[key_pos]
    return keystream
    
def fake_rc4(plaintext, k):
    keystream = get_prg(len(plaintext),k)
    return "".join([chr(ord(a)^ord(b)) for a,b in zip(plaintext,keystream)])
