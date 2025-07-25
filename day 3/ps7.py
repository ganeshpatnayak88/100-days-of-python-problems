
# Replace all negative numbers in a list with 0.

s=[2,-1,-3,2,-7,8,0]
s_new=[]
for i in range(0,len(s)):
    if s[i]<0:
        s_new.append(0)
    else:
        s_new.append(s[i])
print(s_new)