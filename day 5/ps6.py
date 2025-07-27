# Find all unique pairs that sum to a given target.

g=[2,3,4,2,4,5]
for i in g:
    for j in g:
            for k in g:
                 if i+j+k==9:
                      print(i,j,k)
