

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<HR>
"""

print(html)

if 'user' in form:
    print(f"Hello, {form['user'].value}")
else:
    print(f"Who are you?")
