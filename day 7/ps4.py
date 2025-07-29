# 5. Extract all numbers from a string and calculate their sum.
#  "abc12xyz34" → Output: 46

f="abc12xyz34"
d=""
v=""
for i in range(0,5):
    if f[i].isdigit():
        d+=f[i]
for j in range(5,len(f)):
    if f[j].isdigit():
        v+=f[j]
print(int(d)+int(v))