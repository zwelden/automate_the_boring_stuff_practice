#! python3
#! phoneAndEmail.py - Finds all phone numbers and email addresses on the clipboard


import re
import pyperclip

phoneRegex = re.compile(r"""(
                             (\(\d{3}\)\s|\d{3})?
                             (\s|\.|-)?
                             (\d{3})
                             (\s|\.|-)
                             (\d{4})
                             (\s*(ext|x|ext\.)\s*(\d{2,5}))?
                             )""", re.VERBOSE)

emailRegex = re.compile(r"""(
                             [a-zA-Z0-9._%+-]+     # username
                             @                     # @ symbol
                             [a-zA-Z0-9.-]+        # domain
                             (\.[a-zA-Z]{2,4})     # dot-something

                             )""", re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
