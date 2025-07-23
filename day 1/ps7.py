
# 7.	 Given a string "Python", create a tuple of ASCII values for each character.
 	# Input b=[[1, 2], [3, 4], [5, 6]]     out put=[1,2,3,4,5,6]
 	# r=[1,2,3,4,] p=[10,20,30,40]   output=[11,12,13,14]

name="PYthon"
for i in name:
    if i.islower() or i.isupper():
        print(ord(i))

L=tuple(ord(i) for i in "PYthon" if i.isupper() or i.islower())
print(L)

b=[[1, 2], [3, 4], [5, 6]]     
put=[]
for i in b:
    put+=i
print(put)

r=[1,2,3,4,] 
p=[10,20,30,40]
for i in r:
    for j in range(10,11):
        print(i+j)

r=[1,2,3,4,] 
p=[10,20,30,40]
res=tuple(i+j for i,j in zip(r,p))
print(res)