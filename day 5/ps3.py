# Return True if the list has duplicates.
g=[3,55,4,44,7,77,8,9,9]
new=[]
for i in g:
    if i not in new:
        new.append(i)
print(new)