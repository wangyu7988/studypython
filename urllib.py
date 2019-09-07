from urllib3 import request

r = request.urlopen('http://httpbin.org')

text = r.read()

print(r.status, r.reason)