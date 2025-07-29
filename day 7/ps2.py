# 3. Check whether two strings are anagrams of each other.
a="silent"
b="listen"
a1=[]
b2=[]
for i in a:
    if a not in a1:
        a1.append(i)
for j in b2:
    if b not in b2:
        b2.append(i)
print(a1.sort()==b2.sort())