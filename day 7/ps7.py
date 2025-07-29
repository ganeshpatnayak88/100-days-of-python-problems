# 9. Print all prime numbers from a list.
ki=[5,8,9,67,87,98,78,45,53]
f=[]
for i in range(0,len(ki)):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        f.append(i)
print(f)