# 10.Convert a string to title case without using .title().
h="hello world i am sai"
g=h.split()
d=""
for i in g:
    d+=i[0].upper()+i[1:]+" "
print(d.strip())