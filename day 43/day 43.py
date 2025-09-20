# ip='he llo wor ld'
# k=''
# for i in ip:
#     if i==" ":
#         pass
#     else:
#         k+=i
# print(k)


# k='hari'
# l=''
# for i in k:
#     l=i+l
# print(l)

# ip='he llo world'
# k=''
# for i in ip:
#     if i==" ":
#         pass
#     else:
#         k=i+k
# print(k)

# ip='my_variable_name'
# l=''
# l+=ip[0].upper()
# for i in range(1,len(ip)):
#     if ip[i-1]=="_":
#         l+=ip[i].upper()
#     elif ip[i]=="_":
#         pass
#     else:
#         l+=ip[i]
# print(l)

# o='myVariableName'
# l=""
# for i in range(0,len(o)):
#     if o[i].isupper():
#         l +="_"+o[i].lower()
#     else:
#         l+=o[i]
# print(l)


# l='myVariable'
# o=''
# o+=l[0].upper()
# for i in range(1,len(l)):
#     o+=l[i]
# print(o)






# p='Myvariable'
# k=''
# for i in range(len(p)):
#     if p[i].isupper():
#         k+=p[i].lower()
#     else:
#         k+=p[i]
# print(k)


# l='MyVariable'
# h=''
# h=l[0].lower()
# for i in range(1,len(l)):
#     if l[i].isupper():
#         h+="_"+l[i].lower()
#     else:
#         h+=l[i]
# print(h)




# l='my_variable_name'
# k=''
# k+=l[0].upper()
# for i in range(1,len(l)):
#     if l[i-1]=="_":
#         k+=l[i].upper()
#     elif l[i]=="_":
#         pass
#     else:
#         k+=l[i]
# print(k)
    



# l='myVariableName'
# j=''
# for i in range(0,len(l)):
#     if l[i].isupper():
#         j+="_"+l[i].lower()
#     else:
#         j+=l[i]
# print(j)

# l='myVariable'
# k=''
# k+=l[0].upper()
# for i in range(1,len(l)):
#     k+=l[i]
# print(k)


# l='MyVariable'
# o=''
# o+=l[0].lower()
# for i in range(1,len(l)):
#     if l[i].isupper():
#         o+="_"+l[i].lower()
#     else:
#         o+=l[i]
# print(o)        


# l="hello world example"
# o=''
# for i in range(len(l)):
#     if l[i-1]==" ":
#         o+=l[i].upper()
#     elif l[i]==" ":
#         pass
#     else:
#         o+=l[i]
# print(o)
        


# z="hello world example"
# o=''
# for i in range(len(z)):
#     if z[i-1]==" ":
#         o+="_"+z[i].upper()
#     elif z[i]==" ":
#         pass
#     else:
#         o+=z[i]
# print(o)


# p="hello world example"
# o=''
# o+=p[0].upper()
# for i in range(1,len(p)):
#     if p[i-1]==" ":
#         o+=p[i].upper()
#     elif p[i]==" ":
#         pass
#     else:
#         o+=p[i]
# print(o)



# l='aabbccaaa'
# c=1
# k=''
# for i in range(1,len(l)):
#     if l[i-1]==l[i]:
#         c+=1
#     else:
#         k+=l[i-1]+str(c)
#         c=1
# k+=l[-1]+str(c)
# print(k)


# l='Hello'
# o=''
# for i in l:
#     if i.isupper():
#         o+=i.lower()
#     else:
#         o+=i.upper()
# print(o)


# l='abc123d4'
# o=''
# for i in l:
#     if i.isalpha():
#         pass
#     else:
#         o+=i
# print(o)

# p='Abc123!@#'
# u=''
# l=''
# s=''
# for i in p:
#     if i.isupper():
#         u+=i
#     elif i.islower():
#         l+=i
#     else:
#         s+=i
# print(u)
# print(l)
# print(s)

# o='Abc@123x!'
# u=''
# l=''
# d=''
# s=''
# for i in o:
#     if i.isupper():
#         u+=i
#     elif i.isdigit():
#         d+=i
#     elif i.islower():
#         l+=i
#     else:
#         s+=i
# print(u)
# print(l)
# print(d)
# print(s)


# l=input("enter:")
# upper=0
# lower=0
# spcl=0
# num=0
# for i in l:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         num+=1
#     else:
#         spcl+=1
# if upper>=1 and lower>=1 and num>=1 and spcl>=1 and len(l)>7:
#     print("it is strong")
# else:
#     print("not strong")


# p='aabbcc'
# l=''
# for i in p:
#     if i not in l:
#         l+=i
# print(l)

# k='aabbccde'
# l=''
# for i in range(1,len(k)):
#     if k[i-1]==k[i]:
#         l+=k[i]
# print(l)

# n='abc'
# n1=''
# for i in n:
#     n1+=chr(ord(i)+1)
# print(n1)