# From a list of names, create a tuple of names that start with the letter 'A' or 'a'
f=["Ajay","ashok","Anwar","ai"]
for i in range(0,len(f)):
    if f[i].startswith("A") or f[i].startswith("a"):
        print(tuple(f[i]))