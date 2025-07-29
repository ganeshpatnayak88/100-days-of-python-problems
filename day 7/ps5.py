# 6. Sort a list in ascending and descending order with out using sort? 
d=[2,4,3,5,6,7,8]
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        if d[i]>d[j]:
            d[i],d[j]=d[j],d[i]
        else:
            d[i],d[j]=d[i],d[j]
print(d)