#  m=10
# n=30
# for i in range(m,n+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(j)


# m=1
# n=10
# s=0
# for i in range(m,n+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         s+=1
# print(s)


# for i in range(1,501):
#     s=str(i)
#     b=0
#     for j in s:
#         b+=int(j)**3
#     if b==i:
#         print(i)

# m=10
# n=25
# for i in range(m,n+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(j)
#         break


# m=10
# n=25
# a=0
# for i in range(m,n+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         a=j
# print(a)


# n='krishna'
# v='aeiou'
# b=''
# for i in n:
#     if i in v:
#         b+=i
#         break
# print(b)

# n='ramakrishna'
# a='aeiou'
# b=''
# for i in n:
#     if i in a:
#         b=i
# print(b)

# for i in range(1,11):
#     if i%2!=0:
#         continue
#     else:
#         print(i)

# for i in range(1,11):
#     if i%2==0:
#         continue
#     else:
#         print(i)

# m=1
# n=10
# prime=0
# compos=0
# for i in range(m,n):
#     if i==1:
#         continue
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         prime+=1
#     else:
#         compos+=1
# print(compos)
# '''***pdf6***'''

# def add(a,b):
#     return a+b
# print(add(2,3))

# def even(num):
#     if num%2==0:
#         return ("even",num)
#     else:
#         return('odd',num)
# print(even(9))

# def check(year):
#     if year%4==0 and year%100!=0:
#         return 'it is leap'
#     else:
#         return 'it is not leap'
# print(check(2020))

# def check(num):
#     if 2>num:
#         return False
#     c=0
#     for i in range(1,num+1):
#         if num%i==0:
#             c+=1
#     if c==2:
#         return 'it is a prime'
#     else:
#         return 'it is not prime'
# print(check(11))


# m=int(input('enter :'))
# n=int(input('enter:'))
# def arm(check):
#     b=0
#     for i in str(check):
#         b+=int(i)**3
#     if b==check:
#         return 'yes'

