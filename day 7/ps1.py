# 2. Convert a string to title case without using .title().
# Input: "python is fun" → Output: "Python Is Fun"
d="python is fun".split()
a=""
for i in range(len(d)):
    a+=d[i].capitalize()+" "
print(a)