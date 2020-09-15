import requests
import json

def get():
    pass #TODO
    url = "http://httpbin.org/status/204"
    r = requests.get(url)
    return r.status_code

def post():
    pass #TODO
    url = "http://httpbin.org/post"
    data = {'x':1,'y':2}
    r = requests.post(url=url,data=data)
    return r
