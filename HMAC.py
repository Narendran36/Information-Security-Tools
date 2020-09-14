from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'

def weak_hmac(m, k, ipad, opad):
    pass # TODO
    s_ipad = bytes(a^b for a,b in zip(k,ipad))
    s_opad = bytes(a^b for a,b in zip(k,opad))
    step1 = s_ipad + m
    HMAC = sha1(step1).hexdigest()
    step2 = s_opad + bytes(HMAC, encoding='utf8')
    HMAC = sha1(step2).hexdigest()
    return HMAC
