__author__ = 'vlovets'
import json

f = open("e:/GitHub/python_01/config.json")
try:
    res = json.load(f)
except ValueError as ex:
    print(ex)
    res = {}
finally:
    f.close()

print(res)
