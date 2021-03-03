

import cgi
form = cgi.FieldStorage()


print('Content-type: text/html\n')
print('<TITLE>CGI 101</TITLE>')
print('<H1>A First CGI Script</H1>')
print('<P>Hello, CGI World!</P>')

temp = dir(form)

for i in temp:
    print('***', i, '***', '<hr>')
    t = getattr(form, i)
    print('\t', t, '<hr>')
