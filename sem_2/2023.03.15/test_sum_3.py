import requests

"""
Необходимо написать апишку, которая возращает
сумму чисел в словаре
"""
host = 'http://127.0.0.1:5000/sum3/'

r = requests.post(host,
                  json={'a': 1, 'b': 2, 'c': 3})

assert r.json() == {'sum': 6}

r = requests.post(host,
                  json={'a': 1, 'b': 2, })

assert r.json() == {'sum': 3}

r = requests.post(host,
                  json={'d': 1, })

assert r.json() == {'sum': 1}
