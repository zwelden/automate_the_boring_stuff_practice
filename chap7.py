import re

phonenum = re.compile(r"\d{3}-\d{3}-\d{4}")

texty = "info info fino 123-456-7890 and 987-654-3210"

to_call = phonenum.search(texty)

print(to_call.group())


phonenum_reg_2 = re.compile(r"(\d{3})-(\d{3}-\d{4})")

texty2 = "lalalal asdfadf 918-432-6723"

call_it = phonenum_reg_2.search(texty2)

print(call_it.groups())

phonenum_with_par = re.compile(r"(\(\d{3}\)) (\d{3}-\d{4})")

texty3 = "trying to find a new number (866) 245-6751 in here"

gonna_call = phonenum_with_par.search(texty3)

print(gonna_call.groups())

print("findalls")
call1 = phonenum.findall(texty)
print(call1)
calls2 = phonenum_reg_2.findall(texty2)
print(calls2)
calls3 = phonenum_with_par.findall(texty3)
print(calls3)

print("piping it")

phonenum_reg_with_pipes = re.compile(r"(?:\(\d{3}\) |\d{3}-)?\d{3}-\d{4}")

texty4 = "numbers to find in here 918-123-4567 and (765) 123-4653 754-3434 ladfa"

ringring = phonenum_reg_with_pipes.findall(texty4)

print(ringring)
print(ringring[0][1])
