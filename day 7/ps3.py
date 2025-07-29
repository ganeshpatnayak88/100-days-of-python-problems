# 4. Convert a string "1a2b3c" to "abc123".
a="1a2b3c"
b=""
c=""
for i in a:
    if i.isdigit():
        b+=i
    else:
        c+=i
print(c+b)