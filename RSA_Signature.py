from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    pass # TODO
    sig = RSA.importKey(private_key)
    return sig.encrypt(str(m).encode(),0)
    
def verify(m, s, public_key):
    pass # TODO
    ver = RSA.importKey(public_key)
    m2 = ver.decrypt(s)
    return m2 == m
