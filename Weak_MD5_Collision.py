from itertools import product
import string
import hashlib


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    d = {}
    possible = list(string.printable)
    for i in range(1,6):
        trails = product(possible,repeat=i)
        for trail in trails:
            trail = ''.join(trail)
            h_comp = weak_md5(trail.encode('utf-8'))
            if h_comp not in d:
                d[h_comp] = trail
            else:
                return trail,d[h_comp]
    return 0 # return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)
