# Reverse a list without using .reverse().
s=[1,3,2,3,2,4]
rev=[]
for i in range(len(s)-1,-1,-1):
    rev.append(s[i])
print(rev)

# method 2:
s=[1,3,2,3,2,4]
s.reverse()
print(s)
