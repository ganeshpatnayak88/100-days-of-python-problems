# 5.	Write code to read and write a text file.
res=open("file.txt","w+")
res.write('hello')
res.seek(0)
a=res.read()
print(a)