# Find all numbers greater than the average.
k=[2,4,3,53,55]
sum=0
for i in k:
    sum+=i
avg=(sum//len(k))
for i in k:
    if i>avg:
        print(i)