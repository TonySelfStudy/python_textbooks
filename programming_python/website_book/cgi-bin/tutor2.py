
text = """Content-type: text/html

<TITLE>CGI 101</TITLE>
<H1>A Thirds CGI Script</H1>
<P>Hello, CGI World!</P>

<table border=1>
"""

print(text)

for i in range(5):
    print('<tr>')
    for j in range(4):
        print(f'<td>{i}.{j}</td>')
    print('</tr>')

print("""
</table>
<HR>
""")