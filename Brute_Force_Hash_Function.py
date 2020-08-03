import string
from itertools import product

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    chars = list(string.printable)
    hash_reqd = simple_hash(s)
    combinations = product(chars,repeat=3)
    for trail in combinations:
        if (simple_hash(trail) == hash_reqd and trail != s):
            return trail
    return 0  # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
