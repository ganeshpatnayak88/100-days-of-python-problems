# Create a new list of only positive numbers.
s=[2,3,4,-2,0,-3,-4,5]
d=[]
for i in s:
    if i>=0:
        print(i)
        d.append(i)
print(d)
