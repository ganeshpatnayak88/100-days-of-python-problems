# 2.Check if a string is a palindrome.
h="ganesh"
rev=""
for i in h:
    rev=i+rev
if h==rev:
    print("yes")
else:
    print("no")