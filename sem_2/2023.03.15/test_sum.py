import requests

host = 'http://127.0.0.1:5000/'
r = requests.post(host,
                  json={'a': 4, 'b': 9})

assert r.json() == {'sum': 13}

r = requests.post(host,
                  json={'a': -4, 'b': -9})

assert r.json() == {'sum': -13}
