# Simple client to debug/test server scripts using http.client

import http.client

server = "localhost"
conn = http.client.HTTPConnection(server)

page = '/cgi-bin/form01.py'
vars = "?first=joe&second=banks"
conn.request("GET", page+vars)

response = conn.getresponse()
print(response.status, response.reason)

data1 = response.read()
print(data1.decode())
