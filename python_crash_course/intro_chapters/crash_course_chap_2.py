# Examples and Notes from Python Crash Course
# Chapters 1 & 2
# Created 2020-04-06
# Last modified 2020-04-07


msg1="Message 1"
msg2="Message 2"
name="linda lovelace"

print(msg1)
print(msg2)
print(name.title())

first_name = "tracy"
last_name = 'lords'
full_name1 = f" {first_name} {last_name} "
full_name2 = f'{first_name} \n \t {last_name}'

print(full_name1.title())
print(full_name2.upper())

print(full_name1.rstrip())
print(full_name1.lstrip())
print(full_name2.strip())

# Examples on Page 25
print("\n Exercise 2-4")
print("**************")
print(full_name1.lower().strip())
print(full_name1.upper().strip())
print(f'{full_name1.title().strip()}\n')

print("\n Exercise 2-5")
print("**************")
person="Babe Ruth"
quote="Never let the fear of striking out keep you from playing the game."
print(f"\"{quote}\"\n\t-{person.upper()}\n")

print("\n Exercise 2-7")
print("**************")
name3="\t \n i've got some whitespce going on \n \t"
print(f"original:'{name3}'")
print(f"lstrip:'{name3.lstrip()}'")
print(f"rstrip:'{name3.rstrip()}'")
print(f"strip:'{name3.strip()}'")

print("\n Exercise 2-8")
print("**************")
a, b, c = 1, 2, 3
print("a b c =", a, b, c)
print("fun with numbers ", 0.2 + 0.1, "\n\n")
#import this
