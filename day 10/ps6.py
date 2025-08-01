# Tuple of numbers between 1 to 20 divisible by both 3 and 5.
d=[]
for i in range(1,21):
    if i%3==0 and i%5==0:
        d.append(i)
print(tuple(d))