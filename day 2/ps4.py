# Delete the second and third items in a list.
a=[1,2,3,4,5,5,6,6,9]
b=len(a)
for i in range(0,b):
    if i==1:
        a.pop(i)
print(a)
