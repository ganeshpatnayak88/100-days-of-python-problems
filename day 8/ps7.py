#  From the string "Hello World", create a set of unique characters.
j="Hello World"
e=""
for i in j:
    if i!=" ":
        e+=i
print(set(e))