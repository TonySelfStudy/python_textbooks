# Based on Programming Python example 15-1 page 1130

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])
print(f'webdir: {webdir}; port: {port}')

os.chdir(webdir)
srvraddr = ('', port)
srvobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvobj.serve_forever()

