
# 1. **Reverse a string**
#    Input: `"python"` → Output: `"nohtyp"`
k="python"
r=""
for i in k:
    r=i+r
print(r)


# 2. **Count vowels in a string**
#    Input: `"hello world"` → Output: `3`
d='hello world'
v='aeiou'
c=0
for i in d:
    if i in v:
        c+=1
print(c)



# 3. **Check if a number is prime**
#    Input: `7` → Output: `"Prime"`
num=7
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("no")



# 4. **Find factorial of a number**
#    Input: `5` → Output: `120`
f=5
h=1
for i in range(1,f+1):
    h*=i
print(h)


# 5. **Sum of digits**
#    Input: `1234` → Output: `10`
f=1234
s=str(f)
sum=0
for i in s:
    sum+=int(i)
print(sum)





# ---

# ## 🔹 List/Array Problems

# 6. **Find the largest number in a list**
#    Input: `[10, 25, 5, 99, 56]` → Output: `99`
f=[10,25,5,99,56]
mx=-float('inf')
for i in f:
    if i>mx:
        mx=i
print(mx)




# 7. **Remove duplicates from a list**
#    Input: `[1,2,2,3,4,4,5]` → Output: `[1,2,3,4,5]`
d=[1,2,2,3,4,4,5]
f=[]
for i in d:
    if i not in f:
        f.append(i)
print(f)



# 8. **Second largest number**
#    Input: `[10, 20, 4, 45, 99]` → Output: `45`
d=[10,20,4,45,99]
f=0
s=0
t=0
f4=0
for i in d:
    if i>f:
        f4=t
        t=s
        s=f
        f=i
    elif i>s and i!=f:
        t=s
        s=i
    elif i>t and i!=s:
        t=i
    elif i>f4 and i!=t:
        f4=i
print(f4)






# 9. **Check if list is sorted**
#    Input: `[1,2,3,4,5]` → Output: `True`
#    Input: `[3,1,2]` → Output: `False`
f=[1,2,3,4,5]
h=[3,2,1]
print(f==sorted(f))
print(h==sorted(h))