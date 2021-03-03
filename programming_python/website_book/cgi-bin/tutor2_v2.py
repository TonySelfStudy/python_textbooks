
temp = """Content-type: text/html

<TITLE>CGI 101</TITLE>
<H1>A Thirds CGI Script</H1>
<HR>
<P>Hello, CGI World!</P>

<table border=1>
"""

text = temp

for i in range(5):
    text += '<tr>\n'
    for j in range(4):
        temp = f'<td>{i}.{j}</td>\n'
        text += temp
    text += '</tr>\n'


temp = """
</table>
<HR>
"""

text += temp

with open("debug.txt", "w") as f:
    f.write(text)

print(text)
