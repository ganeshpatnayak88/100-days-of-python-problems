# Print all elements > 25 from the list.
a=[2,5,344,33,22,55,33,55]
b=[]
for i in range(0,len(a)):
    if a[i]>=25:
        b.append(a[i])
print(b)
