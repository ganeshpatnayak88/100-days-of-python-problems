#  4.	Generate a tuple of prime numbers between 10 to 50 using comprehension.

j=[8,9,5,6,7,8]
new=[]
for i in j:
    count=0
    for k in range(1,i+1):
        if i%k==0:
            count+=1
    if count==2:
        new.append("prime")
    else:
        new.append("not prime")
print(new)