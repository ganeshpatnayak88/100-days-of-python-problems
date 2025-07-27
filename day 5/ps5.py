# Find all pairs in a list that sum to 10.
a=[3,4,6,8,9,0,3]
for i in a:
    for j in a:
        if i+j==10:
            print(i,j)