# Check if a list is a palindrome.
num=123
d=str(num)
rev=""
for i in d:
    rev=i+rev
if num==rev:
    print("yes")
else:
    print("no")