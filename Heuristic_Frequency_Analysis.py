def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    pass # return boolean
    frequent = ['e', 't', 'a', 'o', 'i', 'n']
    if is_ascii(s):
        d = {}
        top3 = []
        s = s.lower()
        for ch in s:
            if ch.isalpha():
                if ch in d:
                    d[ch] = d[ch] + 1
                else:
                    d[ch] = 1
        d_order = sorted(d.items(),key=lambda x: x[1],reverse=True)[:3]
        print(d_order)
        if d_order == []:
            return False
        for x in d_order:
            if x[0] not in frequent:
                return False
        return True
