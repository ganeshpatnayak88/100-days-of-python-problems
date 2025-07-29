# 7. Find the second largest number in a list.
first=0
second=0
f=[1,3,6,89,67,90]
for i in f:
    if i>first:
        second=first
        first=i
    else:
        second>i and i==first
        second=i
print(second)