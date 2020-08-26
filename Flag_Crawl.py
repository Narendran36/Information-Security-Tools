import requests

path = ''
host = 'http://10.10.169.100:3000/'
flag = ''
while True:
        response = requests.get(host + path)
        json_response = response.json()
        con_json = json_response
        flag += con_json["value"].encode('ascii')
        path = con_json["next"]
        if con_json["value"] == 'end' and con_json["next"] == 'end':
                break
print(flag)
