# 6.	Find the sum and average of elements in a list.
d=[1,2,3,4,4,5,2]
sum=0
avg=0
for i in d:
    sum+=i
    avg=sum/len(d)
print(avg)
print(sum)