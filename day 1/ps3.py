# 3.	 From a list of names, create a tuple of names that start with the letter 'A' or 'a' 

# s=["amma","amaravati","apple","box","Asking","boy"]
# for i in s:
#     if i[0]=="a" or i[0]=="A":
#         print(tuple(i))
# method 2:
names=["ashok","ajay","vijay","jagga"]
l=tuple(i for i in names if i[0]=="a")
print(l)