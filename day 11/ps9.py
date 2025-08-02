# 9.Find the longest word in a sentence.
s="raviteja is goodddddff boy"
d=s.split()
long=d[0]
for i in d:
    if len(i)>len(d):
        long=i
print(long)