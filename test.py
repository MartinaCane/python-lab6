import requests

base_url = 'http://localhost:5000'


def list():
    url = base_url+'/tasks'
    r = requests.get(url)
    print(r.json())
    print(r)
    return r.json()


list()