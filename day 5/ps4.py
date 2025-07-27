# Return list of elements that appear more than once.
g=[3,2,3,4,6,3,54]
new=[]
dupli=[]
for i in g:
    if i not in new:
        new.append(i)
    else:
        dupli.append(i)
print(dupli)