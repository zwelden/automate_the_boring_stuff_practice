#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
#        mcb.py <keyword> - Loads keyword to clipboard
#        mcb.py list - Loads all keywords to clipboard

import shelve, pyperclip, sys

with shelve.open('mcb') as mcbShelf:

    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcbShelf.clear()
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
