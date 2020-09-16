import hashlib
def sign(line):
    pass
    return hashlib.sha1(line).hexdigest()[:20]

def scan(paths, signature):
    pass
    anomalous_paths = []
    for path in paths:
        with open(path) as f:
            for line in f:
                line = line.rstrip('\n')
                line = line.encode('utf-8')
                if sign(line) == signature:
                   anomalous_paths.append(path) 
                   break
    return anomalous_paths
