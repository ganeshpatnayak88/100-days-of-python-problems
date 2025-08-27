# num=int(input("enter "))
# if num%2==0:
#     print("even")

# num=int(input("enter"))
# def che(num):
   
#     b=1
#     for i in range(1,num+1):
#         b*=i
#     print(b)
# che(num)



# f=[4,5,6,78]
# sum=0
# for i in f:
#     sum+=i
# print(sum)


# f=[2,3,4,5,6]
# j=[4,5,6,38,90]
# l=[]
# for i in f:
#     if i in j:
#         l=l+[i]
# print(l)

# a=10
# b=9
# a,b=b,a
# print(a,b)
        




# def fact(n):
#     a,b=0,1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b
# fact(10)



# list1=[1,2,3,4,5]
# list2=[1,3,5,7,9]
# new=[]
# for i in list1:
#     if i in list2:
#         new+=[i]
# print(new)


# def check(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True


# print(check(5))


# num=12366
# rev=0
# while num>0:
#     rev=num%10+rev*10
#     num=num//10
# print(rev)


# a=['teja','python']
# new=[]

# for i in a:
#     rev=''
#     for j in i:
#         rev=j+rev
#     new=new+[rev]    
# print(new)


# l=[1,2,3]
# sum=''

# for i in l:
#     sum=sum+str(i)
# sum=int(sum)+1
# new=[]
# for i in str(sum):
#     new.append(int(i))
# print(new)
# # new=[]
# i=11
# while i>sum:
#     new=[i-sum]+new
#     i-=1
    


# def check(num):
#     count=0
#     if 2>num:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True

#     high=num
#     count=0
#     while count<6:
#         if check(5) and count<6:
#             print(high)
#             high+=1
#         count+=1

# check(num=5)
    

# f=[3,3,4]
# k=""
# s=0
# for i in f:
#     k+=str(i)
# s=int(k)+1
# f=[]
# for i in str(s):
#     f=f+[int(i)]
# print(f)









# f=[9,9,9]
# g=""
# s=0
# for i in f:
#     g+=str(i)
# s=int(g)+1
# o=[]
# for i in str(s):
#     o=o+[int(i)]
# print(o)
"***here a num is prime or not***"
# def check(num):
#     if 2>num:
#         return False
#     count=0
#     for i in range(1,num+1): #if here when you give range(2,num) then count=0 take
#         if num%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False

'****nearest prime number****'
# num=int(input("enter:"))
# high=num+1
# low=num+1
# if check(num):
#     print(num)
# else:
#     while True:
#         if check(high):
#             print(high)
#             break
#         elif check(low):
#             print(low)
#             break
#         high+=1
#         low-=1
"****can enter number then give output as that prime numbers****"
# num=int(input("enter"))
# high=1
# c=0
# while c<num:
#     if check(high):
#         print(high)
#         c+=1
#     high+=1


# h="pprogramming"
# k=""
# for i in h:
#     if h.count(i)==1:
#         k+=i
#         break
# print(k)





# def check(num):
#     if 2>num:
#         return False
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False

# num=int(input("enter a num"))
# high=num+1
# low=num-1
# if check(num):
#     print(num)
# else:
#     while True:
#         if check(high):
#             print(high)
#             break
#         elif check(low):
#             print(low)
#             break
#         high+=1
#         low-=1

# num=int(input("enter a num"))
# high=1
# c=0
# while c<num:
#     if check(high):
#         print(high)
#         c+=1
#     high+=1


# f=3
# n=1
# for i in range(1,f+1):
#     n*=i
# print(n)



