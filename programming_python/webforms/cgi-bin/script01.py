# example of a cgi script to inspect with a python client

import logging
import cgi
from tony_util.dir_diagnostics import values

logging.basicConfig(filename='server.log',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s| %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Running script01')

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<TITLE>CGI 101</TITLE>')
print('<H1>A First CGI Script</H1>')
print('<P>Hello, CGI World!</P>')

print('<hr>')

print(f'{form=}')





usage = """
# from example at: https://docs.python.org/3/library/http.client.html
# note HTTPSConnection changed to HTTPConnection
import http.client
conn = http.client.HTTPConnection("localhost")
conn.request("GET", "/cgi-bin/script01.py")
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()  # This will return entire content.
print(data1.decode)
"""

# print(f'{usage}')
