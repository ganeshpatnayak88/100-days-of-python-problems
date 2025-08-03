# Check if any 2 numbers in list add to 100.
h=[55,10,90,76,45,65,35]
for i in h:
    for j in h:
        if i+j==100:
            print(i,j)