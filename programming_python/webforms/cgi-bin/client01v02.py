# Simple client to debug/test server scripts using requests

import requests
from tony_util.dir_diagnostics import values

page = 'http://localhost/cgi-bin/form01.py'
query = {'first': 'joe', 'second': 'banks'}

req = requests.get(page, params=query)

print(req)
values(req)

# print(req.json())
