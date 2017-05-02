import os
import shelve

with open("./chap8_test.txt") as f:
    hello_content = f.read()
print(hello_content)

with open("./sonnet29.txt") as f:
    content = f.readlines()
print(content)

with open("bacon.txt", "w") as f:
    f.write("Hello World!\n")

with open("bacon.txt", "a") as f:
    f.write("Bacon is not a vegetable.")

with open("bacon.txt") as f:
    content2 = f.read()
print(content2)

print(hello_content)

with shelve.open("mydata") as shelfFile:
    shelfFile['cats'] = ["Zophie", "Pooka", "Simon"]
    print(shelfFile['cats'])
