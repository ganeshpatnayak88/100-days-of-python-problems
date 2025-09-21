# o=[1,2,3]
# o.append(4)
# print(o)    

# p=[1,2,3,4]
# # p.remove(3)
# p.pop(2)
# print(p)

# k=[4,7,1,9]
# max=-float('inf')
# for i in k:
#     if i>max:
#         max=i
# print(max)

# k=[4,7,1,9]
# min=float('inf')
# for i in k:
#     if i<min:
#         min=i
# print(min)


# o=[1,2,3]
# s=0
# k=sum(o)
# print(k)
# for i in o:
#     s+=i
# print(s)

# d=[1,2,3,2,23,23,23,23,23,2,2]
# k=''
# for i in d:
#     if d.count(i)>2:
#         k+=str(i)
#         break
# print(k)
        
# k=[1,2,3,4]
# k.reverse()
# print(k)
# l=k[::-1]
# print(l)
# o=[]
# for i in range(len(k)-1,-1,-1):
#     o=o+[k[i]]
# print(o)
    
# o=[4,1,3,2]
# o.sort()
# print(o)
# l=sorted(o)
# print(l)

# o=[1,2,2,3]
# k=[]
# for i in o:
#     if i not in k:
#         k=k+[i]
# print(k)


# a,b=[1,2],[3,4]
# print(a+b)
# a.extend(b)
# print(a)

# k=[1,2,3]
# l=[2,3]
# o=[]
# for i in k:
#     if i in l:
#         o=o+[i]
# print(o)
        
# l=[1,2,3,4]
# k=[]
# for i in l:
#     if i%2==0:
#         k=k+[i]
# print(k)
        
# l=[1,2,3,4]
# k=[]
# for i in l:
#     if i%2!=0:
#         k=k+[i]
# print(k)

# l=[1,2,1]
# o=[]
# if l==l[::-1]:
#     print("yes")
# else:
#     print("no")
    

# l=[0,-1,2,-3,4]
# p=0
# n=0
# z=0
# for i in l:
#     if i>0:
#         p+=1
#     elif i<0:
#         n+=1
#     else:
#         z+=1
# print(p,n,z)


# d=[1,3,4,5,0]
# f=0
# s=0
# for i in d:
#     if i>f:
#         s=f
#         f=i
#     elif i>s and f!=i:
#         s=i
# print(s)

# o=[5,1,4,2,3]
# f=float("inf")
# s=float("inf")
# for i in o:
#     if i<f:
#         s=f
#         f=i
#     elif i<s and f!=i:
#         s=i
# print(s)


# j=[1,2,3]
# p=j.copy()
# print(p)

# p=[1,2,3,4,5]
# l=[]
# for i in p:
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         l=l+[j]
# print(l)
        
# p=[0,2,0,4]
# for i in range(len(p)):
#     if p[i]==0:
#         p[i]=-1
# print(p)

# p=[5,5,5,5,5]
# o=[]
# for i in range(len(p)):
#     if p[0]==p[i]:
#         o.append(p[i])
# if list(o)==list(p):
#     print("true")
# else:
#     print("flase")
        

# for i in range(1,6):
#     n=65
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#     print()



# for i in range(1,6):
#     n=65
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#         n+=1
#     print()

# n=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#         n+=1
#     print()

# c=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c+=1
#     print()
       

# num=1
# for i in range(1,6):
#     m=num
#     for j in range(1,i+1):
#         print(m,end='')
#         m-=1
#     print()
#     num+=1
# 
# 
# n=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n),end="  ")
#     n+=1
#     print()

# n=69
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n),end="")
#     n-=1
#     print()


# n=input("enter:")
# if ord(n)>=65 and ord(n)<=90:
#     print("captail")
# elif ord(n)>=97 and ord(n)<=122:
#     print("small")
# elif ord(n)>=48 and ord(n)<=57:
#     print("numaric")
# else:
#     print("special")


# m=90
# n=65
# r=int(input('enter:'))
# for i in range(1,int(r)+1):
#     for j in range(1,i+1):
#         if i<=2:
#             print(j,end=" ")
#         elif i==3:
#             print(chr(n),end=" ")
#         elif i==4:
#             print(chr(m),end=' ')
#         else:
#             print("* ",end=" ")
#     print()


# c=1
# n=97
# r=input("enter:")
# for i in range(1,int(r)+1):
#     for j in range(1,i+1):
#         if i%2!=0:
#             print(c,end=" ")
#             c+=1
#         else:
#             print(chr(n),end=" ")
#             n+=1
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# s='aabbccaaa'
# c=1
# o=''
# for i in range(1,len(s)):
#     if s[i-1]==s[i]:
#         c+=1
#     else:
#         o+=s[i-1]+str(c)
#         c=1
# o+=s[-1]+str(c)
# print(o)

# out=[]
# d=[121,333,421,563,454]
# for i in range(len(d)):
#     c=0
#     rev=''
#     s=str(d[i])
#     for j in s:
#         rev=j+rev
#         c+=int(j)
#     if rev==s:
#         out.append(c)
# print(out)


# name="manoj"
# k=''
# for i in range(len(name)):
#     k+=chr(ord(name[i])+1)
# print(k)



    
# d="abcde"
# t='bd'
# o=[]
# f=True
# for i in t:
#     c=0
#     for j in d:
#         if i==j:
#             c+=1
#             o.append(c)
#         else:
#             c+=1
# if (o[1]-o[0])>=0:
#     f=True
# else:
#     f=False
# print(f)


# s='myName'
# c=''
# for i in range(len(s)):
#     if s[i].isupper():
#         c+='_'+s[i]
#     else:
#         c+=s[i]
# print(c)
   




# num = 12
# numbers = [1000, 900, 500, 400, 100, 90,
#            50, 40, 10, 9, 5, 4, 1]
# romans  = ["M", "CM", "D", "CD", "C", "XC",
#            "L", "XL", "X", "IX", "V", "IV", "I"]
# result = ""
# for i in range(len(numbers)):
#     while num >= numbers[i]:
#         result = result + romans[i]
#         num = num - numbers[i]
# print("Roman numeral:", result)


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print("* ",end="")
#     print()
