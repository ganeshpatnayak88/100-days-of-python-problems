

# 9.	Tuple of product of pairs (i * j) where:
# •	i in [2, 4, 6]
# •	j in [1, 3, 5]

i=[2,4,6]
j=[1,3,5]
for x in i:
    for k in j:
        print(x*k)

i=[2,4,6]
j=[1,3,5]
for a,b in zip(i,j):
    print(a*b)
