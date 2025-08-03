# Count number of such valid pairs in a list.
j=[7,8,9,5]
for i in range(0,len(j)):
    for o in range(i+1,len(j)):
        print(j[i],j[o])