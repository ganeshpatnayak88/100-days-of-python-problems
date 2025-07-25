# Find the average of numbers in a list.

s=[2,45,34,23,25,89]
sum=0
avg=0
for i in s:
    sum+=i
    avg=sum//len(s)
print(avg)