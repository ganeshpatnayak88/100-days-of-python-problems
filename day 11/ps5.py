# 5.Remove all ($)  punctuation from a string.
f="sai$ganesh"
d=""
for i in f:
    if i!="$":
        d+=i
print(d)