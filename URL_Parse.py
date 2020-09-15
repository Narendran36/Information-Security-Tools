# imports go here
from urllib.parse import urlparse

def parse_url(url):
    pass # TODO
    o = urlparse(url)
    return o.scheme,o.netloc,o.path
