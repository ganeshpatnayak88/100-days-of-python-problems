# 7.Find the first non-repeating character in a string.
d="1,1,2,2,3,4,76,89"
f={}

for i in d:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
for i in f:
    if f[i]==1:
        print("non-repeating",i)
        break
else:
    print("not found")