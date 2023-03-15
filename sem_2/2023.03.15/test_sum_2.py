import requests

"""
Необходимо написать апишку, которая возращает
сумму чисел в массиве
"""
host = 'http://127.0.0.1:5000/sum2/'

r = requests.post(host,
                  json={'data': [1, 2, 3]})

assert r.json() == {'sum': 6}

r = requests.post(host,
                  json={'data': [-1, -2, -3]})

assert r.json() == {'sum': -6}
