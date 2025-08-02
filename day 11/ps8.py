# 8.Count the frequency of each character in a string.
d="a,d,c,g,h,s,f,"
b={}
for char in d:
    if char in b:
        b[char]+="1"
    else:
        b[char]="1"
for char in b:
    print(char,":",b[char])