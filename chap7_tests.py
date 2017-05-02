import re

def is_strong_password(string):
    #length > 8
    #uppercase and lowercase
    #at lease one digit
    length_regex = re.compile(r".{8,}")
    uppercase_regex = re.compile(r"[A-Z]+")
    lowercase_regex = re.compile(r"[a-z]+")
    digit_regex = re.compile(r"[0-9]+")

    length = length_regex.search(string)
    upper = uppercase_regex.search(string)
    lower = lowercase_regex.search(string)
    digit = digit_regex.search(string)
    if length != None and upper != None and lower != None and digit != None:
        return True
    else:
        return False

def str_strip(string):
    leading_ws_strip_reg = re.compile(r"^[\t\s]+")
    tailing_ws_strip_reg = re.compile(r"[\t\s]+$")

    leading = leading_ws_strip_reg.search(string)
    tailing = tailing_ws_strip_reg.search(string)
    if leading != None:
        string = leading_ws_strip_reg.sub("", string)
    if tailing != None:
        string = tailing_ws_strip_reg.sub("", string)

    return string





q20_regex = re.compile(r"(\d{1,3}(?:,\d{3})*)")

q20_string = "stuff numbers 42 1234 1,234 12,34,567 6,368,745 lalal"

q20_result = q20_regex.findall(q20_string)

print(q20_result)


q21_regex = re.compile(r"[A-Z][a-z]+\sNakamoto")

q21_string1 = "Satoshi Nakamoto"
q21_string2 = "Alice Nakamoto"
q21_string3 = "Robocop Nakamoto"
q21_string4 = "Mr. Nakamoto"
q21_string5 = "satoshi Nakamoto"
q21_string6 = "Nakamoto"
q21_string7 = "Satoshi nakamoto"

q21_result1 = q21_regex.search(q21_string1)
q21_result2 = q21_regex.search(q21_string2)
q21_result3 = q21_regex.search(q21_string3)
q21_result4 = q21_regex.search(q21_string4)
q21_result5 = q21_regex.search(q21_string5)
q21_result6 = q21_regex.search(q21_string6)
q21_result7 = q21_regex.search(q21_string7)

print(q21_result1.group())
print(q21_result2.group())
print(q21_result3.group())
print(q21_result4 == None)
print(q21_result5 == None)
print(q21_result6 == None)
print(q21_result7 == None)

q22_regex = re.compile(r"(?:alice|bob|carol)\s(?:eats|pets|throws)\s(?:apples|cats|baseballs)\.", re.IGNORECASE)

q22_string1 = "Alice eats apples."
q22_string2 = "Bob pets cats."
q22_string3 = "Carol throws baseballs."
q22_string4 = "Alice throws Apples."
q22_string5 = "BOB EATS CATS."
q22_string6 = "Robocop eats apples."
q22_string7 = "ALICE THROWS FOOTBALLS."
q22_string8 = "Carol eats 7 cats."

q22_result1 = q22_regex.search(q22_string1)
q22_result2 = q22_regex.search(q22_string2)
q22_result3 = q22_regex.search(q22_string3)
q22_result4 = q22_regex.search(q22_string4)
q22_result5 = q22_regex.search(q22_string5)
q22_result6 = q22_regex.search(q22_string6)
q22_result7 = q22_regex.search(q22_string7)
q22_result8 = q22_regex.search(q22_string8)

print(q22_result1.group())
print(q22_result2.group())
print(q22_result3.group())
print(q22_result4.group())
print(q22_result5.group())
print(q22_result6 == None)
print(q22_result7 == None)
print(q22_result8 == None)


print(is_strong_password("abcdefg")) # False
print(is_strong_password("Abcdefg1")) # True
print(is_strong_password("123456789")) # False
print(is_strong_password("asd123AGJ")) # True


string1 = "   Hello World    "
string2 = "     Tabs Tabs Tabs      "
string3 = "Nothing to strip"
string4 = " 234easdfs "
string5 = "    leading only"
string6 = "tailing only     "

print(str_strip(string1))
print(str_strip(string2))
print(str_strip(string3))
print(str_strip(string4))
print(str_strip(string5))
print(str_strip(string6))
