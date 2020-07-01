alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    pass #print all (plaintext, k) possibilities and copy the right one to the Edx platform
    for i in range(0,26):
        print(decrypt(ciphertext, i), " ", i)
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
