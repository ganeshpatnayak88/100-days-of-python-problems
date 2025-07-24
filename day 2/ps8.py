
# Find the max and min number in a list.
# method 1:
s=[1,2,3,4,56,23,20]
max=[]
min=[]
b=s[0]
for i in s:
    if i>=b:
        b=i
max.append(b)
print(max)
for i in s:
    if i<=b:
        b=i
min.append(b)
print(min)
# method 2:
s=[1,2,3,4,56,23,20]
d=s[0]
for i in range(0,len(s)):
    if d<=s[i]:
        d=s[i]
print(d)