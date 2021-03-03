# Based on tutorial at:
# https://www.w3schools.com/html/html_forms.asp


import cgi
from tony_util.dir_diagnostics import values

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<TITLE>Forms 101</TITLE>')
print('<H1>Learning about Forms</H1>')

print('<P>User form data below.</P>')

print(f'First Name: {form["first"].value}<br>')
print(f'Second Name: {form["second"].value}<br>')
print(f'Gender: {form["gender"].value}<br>')
print(f'Age: {form["age"].value}<br>')

checks = ["check1", "check2", "check3"]
for c in checks:
    if c in form:
        print(f'Checkbox: {form[c].value}<br>')


print('<hr>')
print('Attributes of form created with "form = cgi.FieldStorage()"<br>')
values(form, "html")
