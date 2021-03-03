# Simple client to debug/test server scripts using requests

import requests
from tony_util.dir_diagnostics import values

page = 'http://localhost/cgi-bin/form01.py'
query = {'first': 'joe', 'second': 'banks'}

method = 'post'

if method == 'get':
    req = requests.get(page, params=query)
elif method == 'post':
    req = requests.post(page, data=query)
else:
    req = None

print(req)
values(req)
