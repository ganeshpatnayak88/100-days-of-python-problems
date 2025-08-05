# 7.	Remove all elements from a list that appear more than once.
d=[1,2,3,4,5,6,7,8,9,1,2,6,7,9,7,8]
c=[]
for i in d:
    if i not in c:
        c.append(i)
print(c)