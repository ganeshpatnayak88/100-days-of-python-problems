# 4.Replace every vowel in a string with '@'.
f="dog"
s="AEIOUaeiou"
re=""
for i in f:
    if i in s:
        re+="@"
    else:
        re+=i
print(re)